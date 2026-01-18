import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables here
load_dotenv()

def generate_report(resume, job_desc):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError("GROQ_API_KEY not found. Check your .env file.")

    client = Groq(api_key=api_key)

    prompt_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "prompts",
        "resume_review.txt"
    )

    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = prompt_template.format(
       resume = resume[:8000],
       job_desc = job_desc[:4000]
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_completion_tokens=1500,
        timeout=60
    )

    return response.choices[0].message.content
