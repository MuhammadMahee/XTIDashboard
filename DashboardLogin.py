import streamlit as st
import base64

# --- Page Config ---
st.set_page_config(page_title="Xclusive Login", layout="centered")

# --- Constants ---
logo_path = "xti_logo.png"
USERNAME = "test"
PASSWORD = "123"
powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiNDFlN2I3OWUtZGM4Zi00MmIzLTg2NGUtMWQ4YWJlZDIwMjRiIiwidCI6IjViN2RiZDllLTk3YWYtNGFiOC04YmM2LWE5MzlhMjJkNWM3NCJ9"

# --- Session State Init ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username_input" not in st.session_state:
    st.session_state.username_input = ""
if "password_input" not in st.session_state:
    st.session_state.password_input = ""

# --- Utility: Load logo as base64 ---
def get_base64_logo(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

base64_logo = get_base64_logo(logo_path)

# --- Login Page ---
if not st.session_state.logged_in:
    st.markdown(
        f"""
        <style>
        .login-card {{
            background-color: #1e1e1e;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            width: 100%;
            max-width: 800px;
            height: 200px;
            margin: 5rem auto;
            text-align: center;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }}
        .login-card h3 {{
            margin: 0;
            color: white;
            display: flex;
            align-items: center;
            font-size: 1.8rem;
            font-weight: 600;
        }}
        .login-card h3 img {{
            width: 80px;
            margin-right: 15px;  /* space between image and text */
            vertical-align: middle;
        }}
        </style>
        <div class="login-card">
            <h3><img src="data:image/png;base64,{base64_logo}" />XCLUSIVE TRADING HOLDINGS LLC</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.form(key="login_form"):
        username = st.text_input("Username", value=st.session_state.username_input)
        password = st.text_input("Password", type="password", value=st.session_state.password_input)
        submit = st.form_submit_button("Login")

        if submit:
            st.session_state.username_input = username
            st.session_state.password_input = password
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
            else:
                st.error("Invalid username or password")

    st.markdown("</div>", unsafe_allow_html=True)

# --- Power BI Page ---
else:
    st.title("Power BI Report")

    st.markdown(
        f"""
        <style>
            .powerbi-iframe {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                border: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                z-index: 999999;
            }}
            .stApp {{
                padding: 0 !important;
                margin: 0 !important;
            }}
        </style>
        <iframe
            class="powerbi-iframe"
            src="{powerbi_url}"
            allowfullscreen="true"
        ></iframe>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username_input = ""
        st.session_state.password_input = ""
