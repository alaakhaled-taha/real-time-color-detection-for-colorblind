# 🎨 Color Detection & Enhancement for Color Vision Deficiency

### *A Perona–Malik-Based Image Processing System*

---

## 📌 Overview

This project presents an intelligent image enhancement system tailored for individuals with **color vision deficiency (CVD)**. By leveraging **Perona–Malik anisotropic diffusion**, the system improves edge clarity and segment precision, making it easier for users to **detect, label, and differentiate colors** that are otherwise challenging to perceive.

---

## 🚀 Key Features

✅ **Color Detection & Classification** – Identifies and labels dominant colors within an image
✅ **Anisotropic Diffusion (Perona–Malik)** – Enhances edges while suppressing background noise
✅ **HSV-Based Filtering** – Isolates color regions using perceptually-relevant color space
✅ **Multi-Label Output** – Supports simultaneous detection of multiple color categories
✅ **User-Guided Annotation** – Allows custom labeling based on individual color perception
✅ **Fast Image Processing** – Optimized for real-time applications

---

## 🧠 System Workflow

1. **Image Acquisition** – Load image or video frame from camera or storage
2. **Color Space Conversion** – Convert RGB to HSV for better color discrimination
3. **Mask Generation** – Apply HSV filters to isolate target hues (e.g., red, green, blue)
4. **Edge-Preserving Smoothing** – Run Perona–Malik diffusion to enhance edges
5. **Feature Extraction** – Identify color clusters and edges
6. **Labeling & Display** – Label identified color regions and render the output

---

## 📊 Technical Methodology

| Component                  | Description                                                          |
| -------------------------- | -------------------------------------------------------------------- |
| **Color Space Conversion** | Converts RGB to HSV for intuitive segmentation by hue and saturation |
| **HSV Masking**            | Filters out non-target colors using defined HSV ranges               |
| **Anisotropic Diffusion**  | Perona–Malik model reduces noise while maintaining sharp edges       |
| **Feature Maps**           | Extracts localized patterns and edges using gradients                |
| **Annotation Layer**       | Enables users to define custom labels or verify predicted labels     |

---

## 🖼️ Output Samples

### 🎯 Original Input Image

![original\_image](https://github.com/user-attachments/assets/9e9875cb-5007-463e-b4b8-eec8fc95b403)

### 🧪 After Perona–Malik Filtering

*Denoised image preserving meaningful structures*
![denoised\_frame](https://github.com/user-attachments/assets/7e0bc268-4cac-4cc4-ba5f-0c0c20f27be4)

### 🎯 Color Masks

* **Green Color Mask**
  ![mask\_for\_GREEN](https://github.com/user-attachments/assets/964fb135-9761-441b-babe-c55f65172a93)
* **Red Color Mask**
  ![mask\_for\_RED](https://github.com/user-attachments/assets/48b71f89-e606-45b6-ac1e-c109da438ff9)

---

## 🔮 Future Directions

* ⚡ Optimize performance for live video and real-time feedback
* 🧠 Integrate deep learning models for adaptive color classification
* 🖥️ Build an interactive GUI for user-driven color selection and preview
* 📲 Extend functionality to smart glasses or mobile platforms for daily use
* 🎯 Support advanced perceptual modeling for various CVD types (protanopia, deuteranopia, tritanopia)

---

## 🛠️ Tech Stack

| Technology     | Purpose                                     |
| -------------- | ------------------------------------------- |
| **Python**     | Core development language                   |
| **OpenCV**     | Image processing & computer vision pipeline |
| **NumPy**      | Efficient matrix operations                 |
| **Matplotlib** | Visualization and debugging                 |

---

## 📄 License

This project is released under the **MIT License**. You are free to use, modify, and distribute it for educational, personal, or research purposes.
