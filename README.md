
# 📦 yolov8-holding-detector

A Flask-based web application that uses [YOLOv8](https://github.com/ultralytics/ultralytics) for real-time detection of people holding objects such as **bottles** or **cups** in images and videos.

![YOLOv8 Badge](https://img.shields.io/badge/YOLOv8-Ultralytics-brightgreen)
![Flask Badge](https://img.shields.io/badge/Flask-Web%20App-blue)
![OpenCV Badge](https://img.shields.io/badge/OpenCV-Detection-orange)

---

## 🚀 Features

- ✅ Upload and process **images or videos**
- ✅ Detect **persons**, **bottles**, and **cups**
- ✅ Determine if a person is **holding** a bottle or cup
- ✅ Display annotated media directly in the browser
- ✅ Download:
  - 🖼 First frame (thumbnail) from video
  - 🎞 The processed video or image

---

## 📸 Example

### 🎥 Video Result

🔗 [Click to view annotated video](https://github.com/Geo-y20/yolov8-holding-detector/blob/main/video%20test.mp4)

> GitHub doesn't allow embedded video previews, but you can click the link above to download or view it.

---

### 🖼 Image Results

**Sample 1**  
![Sample 1](https://github.com/Geo-y20/yolov8-holding-detector/blob/main/sample1.png?raw=true)

**Sample 2**  
![Sample 2](https://github.com/Geo-y20/yolov8-holding-detector/blob/main/sample%202.png?raw=true)

---

## 🧠 Model Used

- **YOLOv8s** from [Ultralytics](https://github.com/ultralytics/ultralytics)
- Detects: `person`, `bottle`, `cup` *(extendable to other classes)*

> ⚠️ The model file `yolov8s.pt` is **excluded** from this repository (see `.gitignore`).  
> Download it manually or automatically during setup.

---

## 🛠 Project Structure

```
yolov8-holding-detector/
│
├── app.py                  # Main Flask application
├── yolov8s.pt              # YOLOv8 model (not included in repo)
├── requirements.txt        # Python dependencies
├── README.md
│
├── static/                 # CSS + JS assets
│   ├── script.js
│   └── styles.css
│
├── templates/
│   └── index.html          # Frontend UI
│
├── uploads/                # Temporary uploaded files
└── results/                # Output annotated media
```

---

## 🧪 Getting Started

```bash
# 1. Create a virtual environment
python -m venv yolo-flask-env
source yolo-flask-env/bin/activate  # or: yolo-flask-env\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download YOLOv8s model
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt

# 4. Run the app
python app.py

# 5. Open in your browser
http://127.0.0.1:5000
```

---

## 📥 Requirements

Install dependencies via:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
flask
opencv-python
ultralytics
```

---

## 💡 Future Ideas

- Add more object categories
- Batch processing (multi-file upload)
- Deploy to Hugging Face Spaces or Render
- Add user login/auth (for multi-user access)

---
