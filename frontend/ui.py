import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------
def login_user(username: str, password: str):
    try:
        response = requests.get(
            f"{BASE_URL}/login",
            auth=(username, password),
            timeout=10
        )
        try:
            data = response.json()
        except ValueError:
            return False, {"detail": f"Non-JSON response from login endpoint: {response.text}"}
        if response.status_code == 200:
            return True, data
        return False, data
    except requests.RequestException as e:
        return False, {"detail": f"Connection error: {str(e)}"}

def send_chat_message(
    username: str,
    password: str,
    message: str,
    role: str,
    employee_id: str
):
    try:
        response = requests.post(
            f"{BASE_URL}/chat",
            auth=(username, password),
            json={
                "message": message,
                "role": role,
                "employee_id": employee_id
            },
            timeout=20
        )
        try:
            data = response.json()
        except ValueError:
            return False, {"detail": f"Non-JSON response from chat endpoint: {response.text}"}
        if response.status_code == 200:
            return True, data
        return False, data
    except requests.RequestException as e:
        return False, {"detail": f"Connection error: {str(e)}"}

# ---------------------------------------------------------
# Session state initialization
# ---------------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "password" not in st.session_state:
    st.session_state.password = ""

if "user_info" not in st.session_state:
    st.session_state.user_info = {}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------------------------------------------------
# UI
# ---------------------------------------------------------
st.title("Employee Chatbot")

if not st.session_state.logged_in:
    st.subheader("Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

    if login_button:
        success, result = login_user(username, password)
        if success:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.password = password
            st.session_state.user_info = result
            st.success(f"Logged in as {result.get('role', '')} - {result.get('employee_id', '')}")
            st.rerun()
        else:
            st.error(result.get("detail", "Login failed"))
else:
    col1, col2 = st.columns([4, 1])

    with col1:
        st.success(
            f"Logged in as {st.session_state.user_info.get('message', st.session_state.username)}"
        )
    with col2:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.password = ""
            st.session_state.user_info = {}
            st.session_state.chat_history = []
            st.rerun()
    #st.write(f"**Role:** {st.session_state.user_info.get('role', '')}")
    #st.write(f"**Employee ID:** {st.session_state.user_info.get('employee_id', '')}")
    st.subheader("Chat")
    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.write(chat["content"])
    prompt = st.chat_input("Ask your question")
    if prompt:
        st.session_state.chat_history.append({
            "role": "user",
            "content": prompt
        })
        success, result = send_chat_message(
            st.session_state.username,
            st.session_state.password,
            prompt,
            st.session_state.user_info.get("role", ""),
            st.session_state.user_info.get("employee_id", "")
        )
        if success:
            bot_reply = result.get("bot_response", result.get("response", "No response received."))
        else:
            bot_reply = result.get("detail", "Something went wrong.")

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": bot_reply
        })
        st.rerun()