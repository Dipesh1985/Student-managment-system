import streamlit as st
import pandas as pd
import ast  # To safely read Python data structures from a file
def editer():
    # Load student data from file
    def load_students():
        try:
            with open("student_data.py", "r") as file:
                data = file.read().strip()  # Read entire file content
                if "students =" in data:
                    data = data.split("students =")[-1].strip()  # Extract list part
                return ast.literal_eval(data)  # Convert string to Python list
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return []

    # Save updated student data to file
    def save_students(students):
        try:
            with open("student_data.py", "w") as file:
                file.write(f"students = {students}")  # Write updated list back to file
            st.success("File Drafted Sucessfully",icon=":material/check_circle:")
        except Exception as e:
            st.error(f"Error saving data: {e}")

    # Load students from file
    students = load_students()

    st.title("Editable Student Table")

    # Ensure students list is not empty
    if not students:
        st.warning("No student data found! Please check student_data.py.")

    # Convert tuple list to DataFrame for editing
    df = pd.DataFrame(students, columns=["Name", "Class", "Section", "Transport", "Student_id", "Aadhaar", "Fee", "Due", "Father_Name", "Mother_Name","Addmission Year","Address","Father Job","Category","DOB"])


    # Editable Table
    edited_df = st.data_editor(df, num_rows="dynamic")

    # Save Button
    if st.button("Save Data",icon=":material/save:"):
        try:
            # Convert DataFrame back to list of tuples
            updated_students = [tuple(row) for row in edited_df.to_numpy()]
            save_students(updated_students)  # Save changes permanently to file
            st.success("Data saved successfully!",icon=":material/check_circle:")
        except Exception as e:
            st.error(f"Error processing updated data: {e}")

