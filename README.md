# MNIST Convolutional Neural Network + Digit Drawing App

This project implements a Convolutional Neural Network (CNN) for handwritten digit recognition with a simple graphical interface for drawing digits.

---

## 🚀 Project Features

- Training a CNN model on the MNIST dataset
- Saving the trained model in `.keras` format
- Saving detailed model information in a text file
- Graphical interface for drawing digits
- Real-time recognition of drawn digits
- Visualization of predicted probabilities (bar chart)
- Display of the processed input image fed into the network
- Centering and normalizing the digit before feeding it to the model

---

## 📂 Project Structure

```
digit_recognition/
│
├── machine_learning/
│   ├── __init__.py
│   ├── config.py
│   ├── data_preprocessing.py
│   ├── model_building.py
│   ├── model_training.py
│   ├── visualization.py
│   ├── model_info_saver.py
│
├── application/
│   ├── __init__.py
│   ├── drawing_app.py
│   ├── recognition_window.py
│
├── common/
│   ├── __init__.py
│   ├── config.py
│
├── models/
│   ├── cnn_model.keras
│   ├── model_info.txt
│
├── train.py
├── app.py
├── README.md
└── requirements.txt
```

---

## ⚙️ How to Run the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

(If there is no `requirements.txt`, manually install:
`tensorflow`, `pillow`, `matplotlib`)

### 2. Train the model (if the saved model is not available yet)

```bash
python train.py
```

This will save the trained model into the `models/` folder.

### 3. Launch the digit drawing application

```bash
python app.py
```

- A drawing window will open where you can sketch digits.
- Two additional windows will appear:
  - Real-time recognition with probability bar chart
  - Processed input image preview

---

## 🛠 Technologies Used

- Python 3.10+
- TensorFlow / Keras
- Matplotlib
- Tkinter
- Pillow (PIL)

---

## 📢 Potential Future Improvements

- Fine-tune the model with custom handwritten digits
- Improve CNN architecture for higher recognition accuracy
- Add a dataset builder by saving drawn digits
- Implement real-time data augmentation during training

---


