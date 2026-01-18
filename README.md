# 📄 Resumio - AI Resume Analyzer

An intelligent resume analysis tool powered by AI that evaluates your resume against job descriptions, providing detailed feedback and ATS (Applicant Tracking System) compatibility scores.

## ✨ Features

- **Resume Upload**: Upload your resume in PDF format
- **Job Description Analysis**: Paste any job description for comparison
- **ATS Score Calculation**: Get a similarity score using BERT-based embeddings (0-1 scale)
- **AI-Powered Report**: Generate detailed analysis using Groq LLM
- **Interactive UI**: Built with Streamlit for easy user interaction

## 🎯 How It Works

1. **Upload Resume**: Submit your resume in PDF format
2. **Enter Job Description**: Paste the target job description
3. **Analysis**: The system performs two parallel analyses:
   - **ATS Score**: Uses BERT embeddings to calculate semantic similarity
   - **Detailed Report**: Uses Groq LLM to provide comprehensive feedback

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **NLP Model**: Sentence-Transformers (all-mpnet-base-v2)
- **LLM**: Groq API
- **PDF Processing**: pdfminer.six
- **Similarity Calculation**: scikit-learn

## 📋 Prerequisites

- Python 3.8+
- Groq API Key (free at [console.groq.com](https://console.groq.com))
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pratheek-git/Resumio-AI-Resume-Analyzer.git
   cd Resumio-AI-Resume-Analyzer
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
   Get your API key from [Groq Console](https://console.groq.com)

## 🏃 Running the Application

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501` in your default browser.

## 📁 Project Structure

```
resume-analyzer-ai/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables (create this)
├── .gitignore               # Git ignore rules
├── prompts/
│   └── resume_review.txt    # LLM prompt template for analysis
├── services/
│   ├── ats_service.py       # ATS scoring using BERT
│   └── groq_service.py      # Groq LLM integration
└── utils/
    ├── pdf_utils.py         # PDF text extraction
    └── score_utils.py       # Score processing utilities
```

## 📖 Usage Example

1. Open the application in your browser
2. Click "Browse Files" and select your resume (PDF format)
3. Paste the job description in the text area
4. Click "Analyze"
5. View your ATS score and detailed AI-generated report

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key for LLM access |

## 📊 Output

The application provides:
- **ATS Score**: A numerical score (0-1) indicating resume-job description alignment
- **Detailed Report**: AI-generated analysis including:
  - Skills alignment (✅/❌/⚠️)
  - Experience relevance
  - Education match
  - Suggestions for improvement

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Pratheek** - [GitHub Profile](https://github.com/pratheek-git)

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - For the amazing web framework
- [Groq](https://groq.com/) - For the powerful LLM API
- [Sentence-Transformers](https://www.sbert.net/) - For BERT embeddings
- [pdfminer.six](https://github.com/pdfminer/pdfminer.six) - For PDF processing

## 📞 Support

If you encounter any issues or have questions, please:
1. Check existing [GitHub Issues](https://github.com/pratheek-git/Resumio-AI-Resume-Analyzer/issues)
2. Create a new issue with detailed description
3. Include steps to reproduce the problem

---

