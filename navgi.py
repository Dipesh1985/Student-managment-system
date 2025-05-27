import streamlit as st
import pandas as pd
from student_data import students
from st_aggrid import AgGrid, GridOptionsBuilder



def Edit():
    st.header("Student Management System", divider=True)

    # Convert student data into DataFrame
    df = pd.DataFrame(students, columns=["Name", "Class", "Section", "Transport", "Student_id", "Addhar", "Fee", "Due", "Father_Name", "Mother_Name","Addmission Year","Address","Father Job","Category","DOB"])

    # Ensure "Class" is treated as a string for filtering consistency
    df["Class"] = df["Class"].astype(str)

    # Configure AgGrid
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection(selection_mode="single", use_checkbox=False)
    gb.configure_grid_options(domLayout='normal')
    gb.configure_columns(filterable=True)
    gb.configure_auto_height(True)
    grid_options = gb.build()

    # Sidebar filters
    with st.sidebar:
        selected_option = st.selectbox("Choose a Class:", ["All", "8", "9", "10", "11", "12"])
        selected_option_section = st.selectbox("Choose a Section:", ["All", "A", "B", "C", "D"])
        selected_option_transport = st.selectbox("Choose a Transport:", ["All", "Bus", "Car", "Train", "Scooter", "Walk", "Bicycle"])
        filter_button = st.button("Filter Data", icon=":material/filter_alt:")  # Button to trigger filtering

    # Filtering function
    def filter_data(df, class_option, section_option, transport_option):
        filtered_df = df.copy()  # Start with full dataset

        if class_option != "All":
            filtered_df = filtered_df[filtered_df["Class"] == class_option]
        if section_option != "All":
            filtered_df = filtered_df[filtered_df["Section"] == section_option]
        if transport_option != "All":
            filtered_df = filtered_df[filtered_df["Transport"] == transport_option]

        return filtered_df

    # Show full data initially
    if "filtered_df" not in st.session_state:
        st.session_state.filtered_df = df  # Store full dataset initially

    # Apply filtering only when the button is clicked
    if filter_button:
        st.session_state.filtered_df = filter_data(df, selected_option, selected_option_section, selected_option_transport)

    # Display the data table
    st.write("Student Records:")
    grid,image=st.columns([0.8,0.2])
    with grid:

        grid_response = AgGrid(st.session_state.filtered_df, gridOptions=grid_options, height=700, width='100%', fit_columns_on_grid_load=True)
    with image:
        st.image()
    selected_row = pd.DataFrame(grid_response["selected_rows"])

    # Show selected student details
    if not selected_row.empty:
        st.write("Selected Student:", selected_row.iloc[0]["Name"])
    else:
        st.write("No student selected!")

# Call the function to display the UI
