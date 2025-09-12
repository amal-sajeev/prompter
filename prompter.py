from fastapi import FastAPI, HTTPException, Query, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from formats import *
from openai import OpenAI
import os
from datetime import datetime


client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

app = FastAPI()

# Allow requests from your frontend (127.0.0.1 and localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000", "http://localhost:8000"],  # frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory='static', html=True))

@app.get("/prompt")
def create_prompt(llm: str, user_request:str):
    try:
        if llm in PROMPTING_GUIDES.keys():
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "developer", "content": f"""
            You are a prompt generator specialized in creating optimized prompts for {llm}.  

            You will be given:
            1. A comprehensive prompting best practices guide for {llm} under the variable PROMPTING_GUIDE
            2. A user request that needs to be transformed into an optimized prompt

            Your task is to analyze the user request and create a high-quality, optimized prompt by applying the specific techniques, templates, and best practices from the PROMPTING_GUIDE.

            Here is the PROMPTING_GUIDE for {llm}:

            {PROMPTING_GUIDES[llm]}

            ### Instructions:

            1. **Analyze the User Request:**
            - Identify the task type (analytical, creative, problem-solving, research, technical, coding, etc.)
            - Determine the complexity level and scope
            - Note any specific requirements or constraints mentioned

            2. **Select Appropriate Techniques from PROMPTING_GUIDE:**
            - Choose the most relevant task-specific template from the guide
            - Apply model-specific optimizations for {llm}
            - Incorporate advanced techniques if the task complexity warrants it

            3. **Structure the Optimized Prompt:**
            - Use the recommended formatting style for {llm}
            - Include context and motivation as specified in the guide
            - Add examples if the task would benefit from multi-shot prompting
            - Apply the core principles (clarity, explicitness, positive framing, etc.)

            4. **Quality Assurance:**
            - Ensure the prompt follows the quality checklist from the guide
            - Verify no conflicting instructions exist
            - Confirm all requirements are clearly specified

            5. **Output Requirements:**
            - Return only the final optimized prompt
            - The prompt should be ready to paste directly into the {llm} chat interface
            - Follow the exact formatting recommendations for {llm} models

            ### Key Reminders:
            - Apply {llm}-specific best practices (e.g., XML formatting for Claude 4, positive instruction framing)
            - Include sufficient context and motivation for better results
            - Be explicit about desired output format and style
            - Use appropriate templates and techniques based on task complexity

            ---

            ### Variables available:
            - PROMPTING_GUIDE → Comprehensive best practices document for {llm}
            - llm → the target LLM family (e.g., Claude, GPT, Gemini)
            - User Request → a free-form natural language instruction from the user

            ---

            ### Output:
            Produce a single, highly optimized prompt that applies the best practices from PROMPTING_GUIDE and is ready to be sent directly to {llm}. DO NOT ADD any notes, commentary, or anything else, ONLY RETURN THE PROMPT.
            """},
                    {
                        "role": "user",
                        "content": user_request,
                    },
                ],
            )
            print(completion.choices[0].message.content)
            return(completion.choices[0].message.content.replace("```",""))
        else:
            raise(HTTPException(500, "Model not supported!"))
    except Exception as e:
        print(f"ERROR on {datetime.now().strftime('%Y_%m_%d')} : {e}")
        return(f"ERROR: {str(e)}")
