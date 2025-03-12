import streamlit as st

clock_placeholder = st.empty()
st.title("Local To-Do list:")

if "task" not in st.session_state:
    st.session_state.task = []

new_task = st.text_input("Add To-Do:")
if st.button("Add"):
    if new_task.strip():
        st.session_state.task.append(new_task.strip())
        st.rerun()
        

st.subheader("List:")
for i,task in enumerate(st.session_state.task):
    col1,col2=st.columns([0.8,0.2])
    col1.write(f"- {task}")
    if col2.button("🗑️", key=f"del_{i}"):
        del st.session_state.task[i]
        st.rerun()


if st.button("Remove all tasks"):
    st.session_state.task.clear()
    st.rerun()


