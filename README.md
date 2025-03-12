# 🌿 Allergenic Parameters Tester 🍄✨

## 📝 Overview  
**Allergenic Parameters Tester** is an online tool designed to analyze the allergenicity of protein sequences. It uses **BLASTp** against a custom allergen database and integrates online allergen prediction tools such as **AllergenFP, AlgPred, and AllerCatPro** to assess potential allergenicity.  

This tool is designed with a **Lana Del Rey aesthetic 🎀**, featuring elegant visuals and a smooth user experience.  

---

## 🎯 Features  
✅ **Upload Protein FASTA Files** (up to 50 sequences)  
✅ **BLASTp search against a custom allergen database**  
✅ **Online allergenicity prediction using APIs**  
✅ **IgE binding simulation (ELISA-based antigenicity score)**  
✅ **Physicochemical properties analysis** (melting point, pH sensitivity, hydrophobicity)  
✅ **Protein family & Gene Ontology annotation**  
✅ **Beautiful UI with vintage aesthetics & cute animations 🎀**  

---

## 🚀 How to Install & Run  

### **1️⃣ Clone the repository**  
```sh
git clone https://github.com/Priyanka01ydv/Allergen-Parameters-tester.git
cd Allergen-Parameters-tester
2️⃣ Set up a virtual environment (Recommended)
sh
Copy
Edit
python -m venv venv
# Activate the virtual environment:
# For macOS/Linux:
source venv/bin/activate  
# For Windows:
venv\Scripts\activate  
3️⃣ Install dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the application
sh
Copy
Edit
python app.py
Then, open http://127.0.0.1:5000/ in your browser to use the tool.

📂 Project Structure
graphql
Copy
Edit
Allergen-Parameters-Tester/
│── static/                # CSS, JavaScript, images, and animations
│── templates/             # HTML files (Lana Del Rey aesthetic UI 🎀)
│── uploads/               # Stores uploaded FASTA files
│── app.py                 # Main Flask application
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation (this file)

🖥️ Technologies Used
Programming Language: Python 🐍
Web Framework: Flask 🌐
Database: Custom BLAST allergen database
APIs: AllergenFP, AlgPred, AllerCatPro

📜 License
This project is licensed under the MIT License.

💌 Contact
Created with ❤️ by Priyanka Yadav
🔗 GitHub: Priyanka01ydv


