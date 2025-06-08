import streamlit as st

# Credentials
USERNAME = "test"
PASSWORD = "123"

powerbi_url = "https://app.powerbi.com/groups/me/reports/bb39f0a4-7e88-4eb8-97d0-f1e3ec93e1b2/60a94c464e86414eb784?experience=power-bi"

# Initialize session state keys
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username_input" not in st.session_state:
    st.session_state.username_input = ""

if "password_input" not in st.session_state:
    st.session_state.password_input = ""

if not st.session_state.logged_in:
    st.title("Login Page")

    # Use st.form to handle login input and submit cleanly
    with st.form(key="login_form"):
        username = st.text_input("Username", value=st.session_state.username_input)
        password = st.text_input("Password", type="password", value=st.session_state.password_input)
        submit = st.form_submit_button("Login")

        if submit:
            # Save inputs in session state to keep them persistent if needed
            st.session_state.username_input = username
            st.session_state.password_input = password

            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                # No rerun needed, page will re-render and show logged in content
            else:
                st.error("Invalid username or password")

else:
    st.title("Power BI Report")

    st.markdown(
        f"""
        <style>
            /* Make the iframe fill the entire viewport */
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

            /* Remove Streamlit default padding/margin around the iframe container */
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
