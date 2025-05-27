

import streamlit as st
import pandas as pd
from navgi import Edit
from Add import add
from PIL import Image
from student_data import students
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from streamlit_option_menu import option_menu
from home import hom
from Edit import editer

# Page configuration (must be the first Streamlit command)


st.set_page_config(
    page_title="Student Managment System",
    page_icon=":material/school:",
    layout="wide",
    menu_items={
        "Get Help": "https://docs.streamlit.io",
        "Report a Bug": "https://github.com/streamlit/streamlit/issues",
        "About": "This is a demo app using Streamlit!"
    }
)


css_file = open("style_element.css").read()
st.markdown(f"<style>{css_file}</style>", unsafe_allow_html=True)

new = option_menu(
    menu_title=None,
    options=["Home", "View", "Add", "Edit"],
    icons=["house", "pen-fill", "database-fill-add", "file-person-fill"],
    orientation="horizontal",
    styles={
        "container": { "top": "0px", "expand": "True"},
        "icon": {"font-size": "20px"},
        "nav-link": {"margin": "0px",},
        "nav-link-selected": {},
    }
)

# Define pages
pages = {
    "Home": hom,
    "View": Edit,
    "Add": add,
    "Edit":editer
}

# Display selected page
if new == "Home":
    pages["Home"]()
elif new == "View":
    pages["View"]()
elif new == "Add":
    pages["Add"]()
elif new == "Edit":
    # You can add the edit functionality here
    pages["Edit"]()
else:
    st.error("There has Been Eror In loading the File Please Refresh",icon=[":material/error:"])

