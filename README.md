#Resumio-ATS-Based-AI-Resume-Analyzer

AI Resume Analyzer is a Streamlit-based application that evaluates a resume against a given job description. It combines ATS-style semantic similarity scoring with AI-generated qualitative feedback to help candidates understand how well their resume matches a specific role.

---

## What this app does

- Extracts text from a resume PDF  
- Compares the resume with a job description using semantic similarity  
- Calculates an ATS-style similarity score  
- Generates an AI-based evaluation with per-skill scoring  
- Provides clear suggestions to improve the resume  

---

## Technologies Used

- Python  
- Streamlit  
- Groq LLM API  
- Sentence Transformers (SBERT)  
- PDFMiner  

---

## Project Structure

AI-Resume-Analyzer/
├── app.py
├── services/
│ └── groq_service.py
├── prompts/
│ └── resume_review.txt
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example


---

## How to Run the Project

1. Clone the repository
```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
Create and activate virtual environment

python -m venv venv
venv\Scripts\activate   # Windows
Install dependencies

pip install -r requirements.txt
Add environment variable
Create a .env file:

GROQ_API_KEY=your_api_key_here
Run the application

streamlit run app.py
Use Case
This project is useful for students and job seekers who want to evaluate and improve their resumes before applying for a role.
