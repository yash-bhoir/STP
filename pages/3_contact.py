import streamlit as st  # pip install streamlit

st.set_page_config(
    page_title="Contact us",
    page_icon="📞",
)

st.header(":mailbox: Contact US!")


contact_form = """
<form action="https://formsubmit.co/sahil.kshirsagar@somaiya.edu" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Enter your name" required>
     <input type="email" name="email" placeholder="Enter your email" required>
     <textarea name="message" placeholder="Enter the message here"></textarea>
     <button type="submit">Submit</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/style.css")