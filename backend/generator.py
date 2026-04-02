import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

FRAMEWORK_MAP = {
    "python": {"fastapi": "FastAPI", "flask": "Flask", "django": "Django REST Framework"},
    "javascript": {"express": "Express.js", "fastify": "Fastify"},
    "go": {"gin": "Gin", "echo": "Echo"},
}

def generate_api(description: str, language: str, framework: str) -> dict:
    framework_name = FRAMEWORK_MAP.get(language, {}).get(framework, framework)

    prompt = f"""You are an expert backend developer. Generate a complete, production-ready REST API.

User wants: {description}
Language: {language}
Framework: {framework_name}

Return ONLY a valid JSON object with exactly these fields, no extra text, no markdown:

{{
  "title": "short name for this API",
  "description": "one sentence describing what this API does",
  "routes": [
    {{
      "method": "GET",
      "path": "/example",
      "description": "what this route does"
    }}
  ],
  "code": "the complete working API code as a single string with \\n for newlines",
  "setup": "step by step setup instructions as a single string with \\n for newlines",
  "dependencies": ["list", "of", "packages", "to", "install"]
}}

Rules for the code:
- Include all imports
- Include a working database setup using SQLite
- Include proper error handling with try/except
- Include CORS middleware
- Include at least 4 routes covering full CRUD
- Add comments explaining each section
- Make it production ready, not a toy example
- Do not use markdown code blocks in the code field"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert API developer. Always respond with valid JSON only. Never include markdown, backticks or extra text."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=4000
    )

    raw = response.choices[0].message.content.strip()

    import json
    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        import re
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            result = json.loads(match.group())
        else:
            raise ValueError("Could not parse AI response as JSON")

    return result