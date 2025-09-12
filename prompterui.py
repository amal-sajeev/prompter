import streamlit as st
import requests
import json
import pyperclip

# =========================
# Streamlit App
# =========================

st.set_page_config(
    page_title="Prompt Optimizer Demo",
    page_icon="✨",
    layout="centered"
)

def copy_click(text):
    pyperclip.copy(text)

# ---- Sidebar ----
st.sidebar.title("⚙️ Settings")
api_url = st.sidebar.text_input("FastAPI Endpoint", "http://localhost:8000/prompt")

st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ using Streamlit")

# ---- Main Header ----
st.title("✨ LLM Prompt Optimizer")
st.markdown("Turn **any request** into a polished, optimized prompt for your favorite LLM family.")

# ---- Model Selector ----
llm_options = ["GPT", "CLAUDE", "GEMINI", "DEEPSEEK", "LLAMA"]
llm_choice = st.selectbox("Select LLM Family", llm_options)

# ---- User Request ----
user_request = st.text_area(
    "📝 Describe your task or request",
    placeholder="e.g., Write a marketing email for a new fitness app"
)

# ---- Submit Button ----
if st.button("🚀 Generate Optimized Prompt", use_container_width=True):
    if not user_request.strip():
        st.warning("Please enter a request first.")
    else:
        with st.spinner("Crafting your optimized prompt... ✨"):
            try:
                response = requests.get(
                    api_url,
                    params={"llm": llm_choice, "user_request": user_request},
                    timeout=60
                )
                if response.status_code == 200:
                    optimized_prompt = response.text.strip('"')  # sometimes comes as quoted string
                    st.success("Optimized Prompt Generated!")
                    st.markdown("### 🎯 Optimized Prompt")
                    
                    st.code(optimized_prompt)
                    

                else:
                    st.error(f"API Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Connection Error: {str(e)}")

# ---- Footer ----
st.markdown("---")
st.caption("⚡ Demo of FastAPI-powered Prompt Optimizer | Streamlit Frontend")
