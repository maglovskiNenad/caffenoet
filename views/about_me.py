import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact Me")
def show_form():
    contact_form()

col1,col2 = st.columns(2,gap="small",vertical_alignment="center")

with col1:
    st.image("./assets/logo.png",width=230)
with col2:
    st.title("Maglovski Nenad",anchor=False)
    st.write("Hello! I am a junior DevOps engineer just starting out in the world of technology,"
    " with a strong passion for learning and exploring DevOps methodologies, tools, and processes."
    " With the goal of contributing to modern IT teams and enhancing their systems, I’m currently "
    "focused on gaining the key knowledge and skills necessary for a successful DevOps career.")

    if st.button("Contact Me"):
        show_form()

st.write("\n")
st.subheader("My Current Experience",anchor=False)

st.write("I am currently working on projects that allow me to develop my understanding of:"
"\n- CI/CD Processes – Working with tools like Jenkins, GitHub Actions, and GitLab CI to automate workflows and speed up the development cycle."
"\n- Docker and Virtualization – Practicing with Docker containers to simplify application deployment and create consistent testing environments."
"\n- Infrastructure as Code (IaC) – Exploring Terraform and Ansible to learn how infrastructure can be efficiently managed and versioned."
"\n- Monitoring and Log Management – Using tools like Prometheus and the ELK stack to monitor system performance and analyze data.")

st.write("\n")
st.subheader("My Goals",anchor=False)

st.write("In the coming months, "
"I plan to:"
"\n- Deepen my knowledge of cloud platforms like AWS, Azure, and GCP."
"\n- Enhance my scripting skills with a focus on Bash and Python for task automation."
"\n- Contribute to open-source projects to gain hands-on experience working with the community and real-world environments."
"\nMy vision is to grow into a DevOps engineer who can contribute to system stability, security, and scalability "
"while continuously improving team collaboration and delivery quality.")

st.write("\n")
st.write("If you’d like to follow my journey or share experiences, feel free to reach out on GitHub!")