🎨 Color Detection & Enhancement for Color Blindness  
A Perona-Malik-Based Image Processing Approach  

📌 Overview  
This project focuses on color detection and enhancement to aid individuals with color blindness in distinguishing and labeling colors. The system processes images using Perona-Malik anisotropic diffusion for edge preservation and improved segmentation, allowing users to label and classify colors they cannot perceive accurately.  

🚀 Features  
✔️ Color Detection – Identifies and labels colors in an image  
✔️ Perona-Malik Diffusion – Enhances edges and reduces noise  
✔️ HSV-Based Masking – Targets specific color ranges  
✔️ Multi-Label Classification – Detects multiple colors in an image    
✔️ User Annotations – Allows users to label their perceived colors  
✔️ Real-Time Processing – Fast and efficient image handling  
 
🖼️ How It Works
1️⃣ Convert Image to HSV  
2️⃣ Apply Masking to target color ranges  
3️⃣ Use Perona-Malik Diffusion for smoothing while preserving edges   
4️⃣ Classify Colors and display labels   
5️⃣ Generate Output Image with enhanced features  

📊 Methodology   
Color Space Conversion: Converts RGB to HSV for better segmentation    
Masking: Filters specific colors to target user-defined hues  
Anisotropic Diffusion (Perona-Malik): Reduces noise while keeping edges sharp  
Mean Map & Feature Extraction: Helps in color differentiation  
Labeling & Annotation: Users can define their own color perception  

🔥 Future Work  
✅ Improve real-time performance for faster processing  
✅ Enhance segmentation algorithms to better separate colors  
✅ Integrate a user-friendly GUI for color selection  
✅ Add machine learning models to refine color classification  
✅ Support mobile implementation for accessibility  

🛠️ Technologies Used  
Python    
OpenCV  
NumPy    
Matplotlib 

📄 License  
This project is licensed under the MIT License. Feel free to modify and use it.  
