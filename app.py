import streamlit as st

# --- Load secrets ---
STORED_PASSWORD = st.secrets["JOB_TRIGGER_PASSWORD"]

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("Login to Unlock Pages")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    with st.form("login_form"):
        entered_password = st.text_input("Enter password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if entered_password == STORED_PASSWORD:
                st.session_state.authenticated = True
                st.success("Successfully authenticated! You can now access other pages.")
            else:
                st.error("Invalid password. Try again.")
else:
    st.success("You're already logged in. Go to the sidebar to access other pages.")