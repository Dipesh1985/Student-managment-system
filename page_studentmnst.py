import streamlit as st
from streamlit_appbar import streamlit_appbar
from navgi import Edit
from Add import add
from Edit import editer
from home_main import home
code_text=open("code_file.txt","r+")

st.set_page_config(layout="wide")

modes = [
    {"name": "Home",
        "icon": "Create"
        },
    {"name": "View",
        "icon": "TableView"
        },
    {"name": "Add",
        "icon": "MenuBook"
        },
    {"name": "Edit",
        "icon": "List"
        },
]

mode = streamlit_appbar(title="Student Management System", modes=modes, logo="streamlit-logo-secondary-colormark-darktext.svg", bgColor="#FFFBF5", txtColor="#000000", height=90, key="mode")
try:
    match mode:

        case "Home":
            home()
           
        case "View":
            Edit()
        case "Add":
            add()
            
        case "Edit":
            editer()
           
except:
    pass

            
