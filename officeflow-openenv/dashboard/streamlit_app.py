import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="OfficeFlow Dashboard", layout="wide")

server_url = "http://localhost:8000"

# ---------- Custom CSS ----------
st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}

.header {
    background-color: #0a1f44;
    padding: 20px;
    border-radius: 10px;
    color: white;
    font-size: 32px;
    font-weight: bold;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}

.metric {
    background-color: #0a1f44;
    padding: 15px;
    border-radius: 10px;
    color: white;
    text-align: center;
    font-size: 20px;
}

button {
    background-color: #1f77ff !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="header">OfficeFlow – AI Workplace Dashboard</div>', unsafe_allow_html=True)
st.write("")

# ---------- Controls ----------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Reset Environment"):
        requests.get(f"{server_url}/reset")

with col2:
    if st.button("Get State"):
        st.session_state.data = requests.get(f"{server_url}/state").json()

with col3:
    action = st.selectbox("Action", [
        "read_email",
        "classify_email",
        "reply_email",
        "schedule_meeting",
        "complete_task"
    ])
    if st.button("Perform Step"):
        requests.post(f"{server_url}/step", json={"action_type": action})
        st.session_state.data = requests.get(f"{server_url}/state").json()

st.write("")

# ---------- Dashboard Metrics ----------
if "data" in st.session_state:
    data = st.session_state.data

    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown(f'<div class="metric">Score<br>{data["score"]}</div>', unsafe_allow_html=True)

    with m2:
        st.markdown(f'<div class="metric">Tasks Completed<br>{data["tasks_completed"]}</div>', unsafe_allow_html=True)

    with m3:
        st.markdown(f'<div class="metric">Step<br>{data["step"]}</div>', unsafe_allow_html=True)

    st.write("")

    # ---------- Emails ----------
    st.subheader("Inbox Emails")
    email_df = pd.DataFrame(data["emails"])
    st.dataframe(email_df, use_container_width=True)

    # ---------- Tasks ----------
    st.subheader("Tasks")
    task_df = pd.DataFrame(data["tasks"])
    st.dataframe(task_df, use_container_width=True)