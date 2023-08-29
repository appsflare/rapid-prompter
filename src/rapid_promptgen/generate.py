import streamlit as st
import openai
import os
from dotenv import load_dotenv
from .common.datasets import add_records
import asyncio

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(layout="wide")

st.title("🎈 Rapid Prompts Generator")
st.subheader("Generate prompt-response pairs from a text with the help of an LLM")


def save_settings():
    """Saves instruction prompt settings in session state

    returns None
    """
    st.session_state["settings_saved"] = True





@st.cache_data
def call_openai_chat_completion(system_prompt: str, text: str):
    """Generates reponse using OpenAI
    system_prompt: system prompt to be used
    text: the text to be used to generate prompt-response for
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        temperature=0,
        max_tokens=3500,
        top_p=0.7,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response["choices"][0]["message"]["content"]


def generate_pairs(system_prompt: str):
    response = None
    generated_pairs = None
    with st.form("prompt_form"):
        text_content = st.text_area(label="Text Content", key="text_content")
        submitted = st.form_submit_button("Generate Prompt-Response Pairs")
        if submitted:
            with st.spinner(text="Generating, Please wait..."):
                response = call_openai_chat_completion(system_prompt, text_content)
            st.success("Generated. Please review the responses below.")

            if response is None:
                return

            with st.chat_message("ai"):
                st.write(response)

            generated_pairs = parse_response(response)

    if generated_pairs is None:
        return

    with st.form("dataset"):
        st.data_editor(generated_pairs)
        clicked = st.form_submit_button("Save Dataset")
        if not clicked:
            return
        add_records(generated_pairs)


def main():
    with st.form("settings_form"):
        system_prompt = st.text_area(
            label="System Prompt",
            value="""You are assisting in creating a training dataset to fine-tune a large language model specifically for instructions related to AgilePoint NX eForm's eFormHelper methods. You will generate multiple prompt-response pairs to cover all scenarios surrounding the given code example. All generated prompt-response pairs will follow the following format,
**Prompt:** Generated prompt
**Response:** Generated response for the respective prompt

For the given code example:
1. Disregard any lines in the code containing "console.log" statements.
2. Ensure comprehensive coverage of all scenarios related to the provided code by providing multiple prompt-response pairs. Generate prompts that encompass "How to...", "What is...", and "How do I..." styles.""",
            placeholder="Intruction prompt to configure the LLM",
            key="system_prompt",
        )

        submitted = st.form_submit_button("Save")
        if submitted:
            save_settings()

    if "settings_saved" not in st.session_state:
        return
    generate_pairs(system_prompt)


main()


# # Iterate through the pairs and extract the prompts and responses
# for i in range(1, len(pairs), 3):
#     prompt = pairs[i].strip()
#     response = pairs[i + 1].strip()

#     # Remove line breaks within the response
#     response = response.replace("\n", " ")

#     # Add the prompt-response pair to the list
#     prompt_response_list.append({"prompt": prompt, "response": response})

# st.data_editor(prompt_response_list)
