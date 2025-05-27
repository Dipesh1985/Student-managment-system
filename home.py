import streamlit as st
from Add import add


def hom():
    css_file = open("style_element.css").read()
    st.markdown(f"<style>{css_file}</style>", unsafe_allow_html=True)
    st.title("Student Managment system")
    row1,row2=st.columns([20000,10000])

    st.header("   ")
    with row1:
        None
    st.markdown("<br><br><br>",unsafe_allow_html=True)
    
  

    


        




   


    
    


    # import streamlit as st
    # import hydralit_components as hc

    # #can apply customisation to almost all the properties of the card, including the progress bar
    # theme_bad = {'bgcolor': '#FFF0F0','title_color': 'red','content_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
    # theme_neutral = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-question-circle'}
    # theme_good = {'bgcolor': '#EFF8F7','title_color': 'green','content_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}

    # cc = st.columns(4)

    # with cc[0]:
    # # can just use 'good', 'bad', 'neutral' sentiment to auto color the card
    # hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good',bar_value=77)

    # with cc[1]:
    # hc.info_card(title='Some BAD BAD', content='This is really bad',bar_value=12,theme_override=theme_bad)

    # with cc[2]:
    # hc.info_card(title='Some NEURAL', content='Oh yeah, sure.', sentiment='neutral',bar_value=55)

    # with cc[3]:
    # #customise the the theming for a neutral content
    # hc.info_card(title='Some NEURAL',content='Maybe...',key='sec',bar_value=5,theme_override=theme_neutral)


