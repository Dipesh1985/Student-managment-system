import streamlit as st

def home():
    img=st.image("download.jpg")
    

    st.markdown(f'''<!DOCTYPE html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stylish Container</title>
    <link rel="stylesheet" href="style_element.css">
   
</head>
<body>
    <div class="container">
        <h2>Elegant Container</h2>
        <p>This container has a beautiful shadow effect on top.</p>
        <button class="button">Hello</button>
    </div>
</body>
</html>''',unsafe_allow_html=True)
