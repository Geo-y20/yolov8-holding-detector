import os
import uuid
import cv2
from random import random
from flask import Flask, request, render_template, send_from_directory
from ultralytics import YOLO

app = Flask(__name__)

# Directories to store uploads and results
UPLOAD_DIR = 'uploads'
RESULTS_DIR = 'results'
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# Load the YOLOv8 model
model = YOLO('yolov8s.pt')

# Check if an object is within a person's bounding box
def person_holding_object(person_box, object_box):
    px1, py1, px2, py2 = person_box
    ox1, oy1, ox2, oy2 = object_box
    return (ox1 > px1 and oy1 > py1 and ox2 < px2 and oy2 < py2)

# Process single image input
def process_image(input_path, output_path):
    image = cv2.imread(input_path)
    results = model(image)[0]
    detections = []

    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = box.conf[0].item()
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        if label in ["person", "bottle", "cup"]:
            detections.append(f"{label} ({conf * 100:.1f}%)")
            color = (0, 255, 0) if label == "person" else (255, 0, 0)
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            cv2.putText(image, f"{label} {conf:.2f}", (x1, y1 - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    cv2.imwrite(output_path, image)
    return detections

# Process video and save annotated output + thumbnail (first frame)
def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    width, height = int(cap.get(3)), int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    detections = []
    frame_saved = False
    thumbnail_path = output_path.replace('.mp4', '_thumb.jpg')

    while True:
        success, frame = cap.read()
        if not success:
            break

        if not frame_saved:
            # Save the first frame as a JPEG thumbnail
            cv2.imwrite(thumbnail_path, frame)
            frame_saved = True

        results = model(frame)[0]
        people = []
        objects = []

        for box in results.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = box.conf[0].item()
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            if label == "person":
                people.append((x1, y1, x2, y2))
            elif label in ["bottle", "cup"]:
                objects.append((x1, y1, x2, y2, label, conf))

        for x1, y1, x2, y2 in people:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, "person", (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        for ox1, oy1, ox2, oy2, label, conf in objects:
            is_held = any(person_holding_object((x1, y1, x2, y2), (ox1, oy1, ox2, oy2)) for (x1, y1, x2, y2) in people)
            text = f"Holding {label}" if is_held else label
            detections.append(f"{text} ({conf * 100:.1f}%)")
            color = (0, 0, 255) if is_held else (255, 0, 0)
            cv2.rectangle(frame, (int(ox1), int(oy1)), (int(ox2), int(oy2)), color, 2)
            cv2.putText(frame, text, (int(ox1), int(oy1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        out.write(frame)

    cap.release()
    out.release()
    return detections

# Main Flask route
@app.route('/', methods=['GET', 'POST'])
def home():
    result_file = None
    detection_text = []

    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_ext = file.filename.rsplit('.', 1)[-1].lower()
            uid = uuid.uuid4().hex
            input_path = os.path.join(UPLOAD_DIR, f"{uid}.{file_ext}")
            output_path = os.path.join(RESULTS_DIR, f"result_{uid}.{file_ext}")
            file.save(input_path)

            if file_ext in ['jpg', 'jpeg', 'png']:
                detection_text = process_image(input_path, output_path)
                result_file = f"result_{uid}.{file_ext}"
            elif file_ext in ['mp4', 'avi', 'mov']:
                detection_text = process_video(input_path, output_path)
                result_file = f"result_{uid}.{file_ext}"
            else:
                return "Unsupported file type."

    return render_template('index.html', result_file=result_file, detections=detection_text, random=random)

# Serve result files (video or image)
@app.route('/results/<path:filename>')
def results(filename):
    return send_from_directory(RESULTS_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
