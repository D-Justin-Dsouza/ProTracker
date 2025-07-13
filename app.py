import streamlit as st
import pandas as pd
import json
import os
from db import init_db, add_task, get_all_tasks
from charts import pie_chart, bar_chart, score_line_chart
from logic import apply_score

init_db()

st.set_page_config(page_title="Productivity Tracker", layout="wide")
st.title('Habit Tracker & Productivity Dashboard')

st.sidebar.header(" Add a Task")
with st.sidebar.form(key="task_form"):
    name = st.text_input("Task Name")
    category = st.selectbox("Category", ["Study", "Work", "Gym", "Social", "Other"])
    hours = st.number_input("Hours Spent", min_value=0.0, step=0.5)
    date = st.date_input("Date")
    submit = st.form_submit_button("Add Task")

    if submit:
        if name and hours > 0:
            add_task(name, category, hours, str(date))
            st.success(f" Task '{name}' added!")
        else:
            st.warning(" Please fill all fields.")

data = get_all_tasks()
df = pd.DataFrame(data, columns=['ID', 'Name', 'Category', 'Hours', 'Date'])
df = apply_score(df)

if not df.empty:
    st.divider()
    st.subheader(" Summary Stats")
    total_hours = df["Hours"].sum()
    total_score = df["Score"].sum()
    num_tasks = len(df)

    col1, col2, col3 = st.columns(3)
    col1.metric(" Tasks", num_tasks)
    col2.metric(" Hours", f"{total_hours:.1f}")
    col3.metric(" Productivity Score", f"{total_score:.1f}")
else:
    st.warning("No tasks available yet.")

st.divider()
st.subheader(" Task Log")
with st.expander("Show Task Table"):
    st.dataframe(df, use_container_width=True)

if not df.empty:
    st.divider()
    st.subheader(" Visual Summary")

    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(pie_chart(df), use_container_width=True)
    with col2:
        st.pyplot(bar_chart(df), use_container_width=True)

    st.subheader(" Productivity Score Over Time")
    st.pyplot(score_line_chart(df), use_container_width=True)
else:
    st.info("Add tasks to view charts.")
