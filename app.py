import streamlit as st
from uoh_software_project_time_report.project import *

GSHEET_URL = "https://docs.google.com/spreadsheets/d/1DNoNf4glcuMxKoVzHVrFo-MktmsVji1wf4IHeraWH84/edit?usp=sharing"

st.set_page_config(page_title="Project Time report", layout="centered")

st.write('XXXXX Add dash board with KPI panels here! (e.g. total time spent, remaining time, velocity, e.t.c)')

st.title("Project Time report!")

pr = Project('keys.json')


form = st.form(key="annotation")
with form:
    cols = st.columns((1, 1))
    author = cols[0].selectbox(
        "Name:", ["",
                  "Arttu I Lehtonen",
                  "Borna Jamali",
                  "Leevi J A Takala",
                  "Matias Tolppanen",
                  "Nella T Nieminen",
                  "Tuula Jakobsson Peralta",
                  "Machihito Mizutani",
                  "Roberto Morabito",
                  "Hiroshi Doyu",
                  "Anastasia C Diseth",
                  ], index=0
    )
    binum = cols[1].text_input("Backlog item # (Daily, Review, Retro, Planning is '0'):")
    cols = st.columns(2)
    date = cols[0].date_input("work date:")
    hours = cols[1].slider("Time spent (hours):", 0.25, 7.5, step=0.25)
    comment = st.text_area("Comment:")
    submitted = st.form_submit_button(label="Submit")

if submitted:
    pr.append([[author, binum, hours, str(date), comment]])
    st.success("Thanks! Your time was recorded.")
    st.balloons()

expander = st.expander("See all records")
with expander:
    st.write(f"Open original [Google Sheet]({GSHEET_URL})")
    st.dataframe(pr.get())
