from fastapi import FastAPI, HTTPException, Query, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from formats import *
from openai import OpenAI
import os
from datetime import datetime
from enum import Enum


client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

app = FastAPI()

# Define allowed languages
class Language(str, Enum):
    ENGLISH = "English"
    BENGALI = "Bengali"
    GUJARATI = "Gujarati"
    HINDI = "Hindi"
    KANNADA = "Kannada"
    MALAYALAM = "Malayalam"
    MARATHI = "Marathi"
    ORIYA = "Oriya"
    PUNJABI = "Punjabi"
    TAMIL = "Tamil"
    TELUGU = "Telugu"

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
def create_prompt(llm: str, user_request: str, language: Language = Language.ENGLISH):
    try:
        if llm in PROMPTING_GUIDES.keys():
            completion = client.chat.completions.create(
                model="gpt-5-mini",
                messages=[
                    {"role": "developer", "content": f"""
            You are a prompt generator specialized in creating optimized prompts for {llm}.  

            You will be given:
            1. A comprehensive prompting best practices guide for {llm} under the variable PROMPTING_GUIDE
            2. A user request that needs to be transformed into an optimized prompt
            3. A target language for the final prompt output

            Your task is to analyze the user request and create a high-quality, optimized prompt by applying the specific techniques, templates, and best practices from the PROMPTING_GUIDE. The generated prompt MUST explicitly instruct the {llm} model to respond in {language.value}.

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
            - **CRITICAL: Include explicit instructions for the model to respond in {language.value}**

            4. **Language Requirements:**
            - The prompt MUST contain clear, explicit instructions that the {llm} model should respond entirely in {language.value}
            - If {language.value} is not English, emphasize that the response should be in {language.value} and NOT in English
            - Include language-specific formatting instructions if relevant to {language.value}

            5. **Quality Assurance:**
            - Ensure the prompt follows the quality checklist from the guide
            - Verify no conflicting instructions exist
            - Confirm all requirements are clearly specified
            - Verify that language instructions are prominently placed and unambiguous

            6. **Output Requirements:**
            - Return only the final optimized prompt
            - The prompt should be ready to paste directly into the {llm} chat interface
            - Follow the exact formatting recommendations for {llm} models
            - The prompt must guarantee that {llm} will respond in {language.value}

            ### Key Reminders:
            - Apply {llm}-specific best practices (e.g., XML formatting for Claude 4, positive instruction framing)
            - Include sufficient context and motivation for better results
            - Be explicit about desired output format and style
            - Use appropriate templates and techniques based on task complexity
            - **MANDATORY: The generated prompt must explicitly instruct {llm} to respond in {language.value}**

            ---

            ### Variables available:
            - PROMPTING_GUIDE → Comprehensive best practices document for {llm}
            - llm → the target LLM family (e.g., Claude, GPT, Gemini)
            - User Request → a free-form natural language instruction from the user
            - Target Language → {language.value}

            ---

            ### Output:
            Produce a single, highly optimized prompt that applies the best practices from PROMPTING_GUIDE, includes mandatory {language.value} response instructions, and is ready to be sent directly to {llm}. DO NOT ADD any notes, commentary, or anything else, ONLY RETURN THE PROMPT.
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
            raise(HTTPException(500,"Model not supported!"))
    except Exception as e:
        print(f"ERROR on {datetime.now().strftime('%Y_%m_%d')} : {e}")
        return(f"ERROR: {str(e)}") 


@app.get("/promptupdate")
def promptupdate(llm: str, prompt: str, user_request: str, language: Language = Language.ENGLISH):
    try:
        if llm in PROMPTING_GUIDES.keys():
            completion = client.chat.completions.create(
                model="gpt-5-mini",
                messages=[
                    {
                        "role": "developer",
                        "content": f"""
                            You are a prompt updater specialized in updating and optimized prompts for {llm} based on the user's request.   
                            You will be given:
                            1. A comprehensive prompting best practices guide for {llm} under the variable PROMPTING_GUIDE
                            2. A user request that needs to be transformed into an optimized prompt
                            3. A prompt that needs to be adjusted according to the user's instructions
                            4. A target language for the final prompt output

                            Your task is to analyze the user request and the old prompt, to create a high-quality, optimized prompt by applying the specific techniques, templates, and best practices from the PROMPTING_GUIDE that properly integrates the user's request. The updated prompt MUST explicitly instruct the {llm} model to respond in {language.value}.

                            Here is the PROMPTING_GUIDE for {llm}:

                            {PROMPTING_GUIDES[llm]}

                            ### Instructions:

                            1. **Analyze the User Request:**
                            - Identify the task type (analytical, creative, problem-solving, research, technical, coding, etc.)
                            - Determine the complexity level and scope
                            - Note any specific requirements or constraints mentioned
                            
                            2. **Analyze the Existing Prompt:**
                            - Understand what the original prompt is trying to do
                            - Compare it with the User's request to see what the issues are and what needs to be changed
                            - Plan what changes to make, change the structure of the prompt as needed to accommodate the user's request
                            - Check if the original prompt has language instructions and update them accordingly

                            3. **Select Appropriate Techniques from PROMPTING_GUIDE:**
                            - Choose the most relevant task-specific template from the guide
                            - Apply model-specific optimizations for {llm}
                            - Incorporate advanced techniques if the task complexity warrants it

                            4. **Structure the Optimized Prompt:**
                            - Use the recommended formatting style for {llm}
                            - Include context and motivation as specified in the guide
                            - Add examples if the task would benefit from multi-shot prompting
                            - Apply the core principles (clarity, explicitness, positive framing, etc.)
                            - **CRITICAL: Include explicit instructions for the model to respond in {language.value}**

                            5. **Language Requirements:**
                            - The updated prompt MUST contain clear, explicit instructions that the {llm} model should respond entirely in {language.value}
                            - If {language.value} is not English, emphasize that the response should be in {language.value} and NOT in English
                            - Include language-specific formatting instructions if relevant to {language.value}
                            - Override any existing language instructions in the original prompt

                            6. **Quality Assurance:**
                            - Ensure the prompt follows the quality checklist from the guide
                            - Verify no conflicting instructions exist
                            - Ensure all changes that the user's request asked for are accounted for in the new prompt
                            - Confirm all requirements are clearly specified
                            - Verify that language instructions are prominently placed and unambiguous

                            7. **Output Requirements:**
                            - Return only the final optimized prompt
                            - The prompt should be ready to paste directly into the {llm} chat interface
                            - Follow the exact formatting recommendations for {llm} models
                            - The prompt must guarantee that {llm} will respond in {language.value}

                            ### Key Reminders:
                            - Apply {llm}-specific best practices (e.g., XML formatting for Claude 4, positive instruction framing)
                            - Include sufficient context and motivation for better results
                            - Be explicit about desired output format and style
                            - Use appropriate templates and techniques based on task complexity
                            - Make sure the new prompt correctly understands and achieves what the user wants
                            - **MANDATORY: The updated prompt must explicitly instruct {llm} to respond in {language.value}**
                            
                            ---

                            ### Variables available:
                            - PROMPTING_GUIDE → Comprehensive best practices document for {llm}
                            - llm → the target LLM family (e.g., Claude, GPT, Gemini)
                            - User Request → a free-form natural language instruction from the user
                            - Original Prompt → the existing prompt that needs updating
                            - Target Language → {language.value}

                            ---

                            ### Output:
                            Produce a single, highly optimized prompt that applies the best practices from PROMPTING_GUIDE, accounts for the user's request, includes mandatory {language.value} response instructions, and is ready to be sent directly to {llm}. DO NOT ADD any notes, commentary, or anything else, ONLY RETURN THE PROMPT.
                            """
                    },
                    {
                        "role": "assistant",
                        "content": prompt
                    },
                    {
                        "role": "user",
                        "content": user_request
                    }
                ]
            )
            print(completion.choices[0].message.content)
            return(completion.choices[0].message.content.replace("```",""))
        else:
            raise(HTTPException(500, "Model not supported!"))
    except Exception as e:
        print(f"ERROR on {datetime.now().strftime('%Y_%m_%d')} : {e}")
        return(f"ERROR: {str(e)}") 