import streamlit as st

about_page = st.Page(page="views/about_me.py",title="About Me",icon=":material/account_circle:",default=True,)

project_1_page = st.Page(page="views/chat_bot.py",title="Chat Bot",icon=":material/smart_toy:",)

project_2_page = st.Page(page="views/dashboard.py",title="Dashboard",icon=":material/bar_chart:",)

project_3_page = st.Page(page="views/another_projects.py",title="Projects",icon=":material/view_apps:")

pg = st.navigation({
    "Info":[about_page],
    "Projects":[project_1_page,project_2_page],
    "Other":[project_3_page],
})

st.logo("assets/logo.png")
st.sidebar.text("Made by magla")

pg.run()