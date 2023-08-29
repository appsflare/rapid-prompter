import streamlit as st

st.set_page_config(
    page_title="Rapid Prompt Gen - Configure",
    page_icon="👋",
)

st.title("Configure the App Parameters")
st.sidebar.success("Select a page above.")


if "argilla_api_key" not in st.session_state:
    st.session_state["argilla_api_key"] = ""
    st.session_state["argilla_workspace"] = ""
    st.session_state["argilla_dataset"] = ""
    st.session_state["argilla_api_url"] = ""

argilla_api_url = st.sidebar.text_input(
    "Argilla API URL", st.session_state["argilla_api_url"]
)

argilla_api_key = st.sidebar.text_input(
    "Argilla API Key", st.session_state["argilla_api_key"]
)
argilla_workspace = st.sidebar.text_input(
    "Argilla Workspace", st.session_state["argilla_workspace"]
)
argilla_dataset = st.sidebar.text_input(
    "Argilla Dataset", st.session_state["argilla_dataset"]
)

submit = st.sidebar.button("Submit")
if submit:
    st.session_state["is_configured"] = True
    st.session_state["argilla_api_url"] = argilla_api_url
    st.session_state["argilla_api_key"] = argilla_api_key
    st.session_state["argilla_workspace"] = argilla_workspace
    st.session_state["argilla_dataset"] = argilla_dataset
    st.sidebar.success("Settings Saved!")
