
## 📦 `yolov8-holding-detector`

A Flask-based web application that uses [YOLOv8](https://github.com/ultralytics/ultralytics) for real-time detection of people holding objects such as **bottles** or **cups** in images and videos.

<p align="center">
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-brightgreen" />
  <img src="https://img.shields.io/badge/Flask-Web%20App-blue" />
  <img src="https://img.shields.io/badge/OpenCV-Detection-orange" />
</p>

---

### 🚀 Features

- ✅ Upload and process **images or videos**
- ✅ Detect **persons**, **bottles**, and **cups**
- ✅ Determine if a person is **holding** a bottle or cup
- ✅ Display annotated media directly in the browser
- ✅ Download:
  - 🖼 First frame (thumbnail) from video
  - 🎞 The processed video or image

---

### 📸 Example

#### Image Upload:
<img src="https://via.placeholder.com/500x280.png?text=Annotated+Image" width="500" alt="Sample Output" />

#### Video Upload:
🎥 Annotated video preview in the browser with bounding boxes and labels.

---

### 🧠 Model Used
- **YOLOv8s** from [Ultralytics](https://github.com/ultralytics/ultralytics)
- Detects: `person`, `bottle`, `cup` *(extendable to other classes)*

> ⚠️ The model file `yolov8s.pt` is not included in the repo. It will be downloaded automatically or must be placed manually in the project root.

---

### 🛠 Project Structure

```
yolov8-holding-detector/
│
├── app.py                  # Main Flask application
├── yolov8s.pt              # YOLOv8 model (excluded from repo)
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

### 🧪 Getting Started

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

### 📥 Requirements

Install dependencies via:

```bash
pip install -r requirements.txt
```

Basic contents of `requirements.txt`:
```txt
flask
opencv-python
ultralytics
```

---

### 💡 Future Ideas

- Add multiple object categories
- Upload multiple files at once
- Deploy to Hugging Face Spaces or Render
- Add login/authentication (for users/admins)

---
