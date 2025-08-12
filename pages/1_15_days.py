import streamlit as st
import requests
import json

# --- Load secrets ---
DATABRICKS_API_URL = st.secrets["DATABRICKS_API_URL"]
DATABRICKS_TOKEN = st.secrets["DATABRICKS_TOKEN"]
JOB_ID_ff = st.secrets["JOB_ID_ff"]
JOB_ID_ep = st.secrets["JOB_ID_ep"]
st.set_page_config(page_title="Trigger Job", page_icon="🚀")

# --- Auth check ---
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("You must login from the home page to access this page.")
    st.stop()

st.title("15 days job schedule")

EMAIL_ADDRESS = st.text_input("Enter email address to recieve notification", 
                              value="anurag.pal@zeptonow.com,himanshu.batra@zeptonow.com")

if st.button("Trigger Job"):
    headers = {
        "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload_ff = {
        "job_id": JOB_ID_ff,
        "notebook_params": {
            "EMAIL_ADDRESS": EMAIL_ADDRESS
        }
    }
    payload_ep = {
        "job_id": JOB_ID_ep,
        "notebook_params": {
            "EMAIL_ADDRESS": EMAIL_ADDRESS
        }
    }
    response_ff = requests.post(DATABRICKS_API_URL, headers=headers, data=json.dumps(payload_ff))
    response_ep = requests.post(DATABRICKS_API_URL, headers=headers, data=json.dumps(payload_ep))
    
    if response_ff.status_code == 200:
        run_id = response_ff.json().get("run_id")
        st.success(f"Job triggered successfully! Run ID: {run_id}")
    else:
        st.error(f"Failed to trigger job. Status: {response_ff.status_code}")
        st.code(response_ff.text)

