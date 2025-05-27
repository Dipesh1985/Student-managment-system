import streamlit as st
from student_data import students

file=open("student_data.py","r+")

def add():
    st.header("Add any Student Or Record", divider=True)
    
    col1, col2, col3 = st.columns(3, gap='large')
    col4, col5, col6 = st.columns(3, gap='large')

    with col1:
        name = st.text_input("Enter The Name:")
    with col2:
        class_new = st.selectbox("Enter The Class:", [8, 9, 10, 11])
    with col3:
        transport = st.selectbox("Enter The Transport", ["Bus", "Car", "Train", "Scooter", "Walk", "Bicycle"])
    with col4:
        a_num = st.text_input("Enter The Aadhaar No.", max_chars=12)
    with col5:
        f_name = st.text_input("Enter Your Father's Name")
    with col6:
        m_name = st.text_input("Enter Your Mother's Name")

    a = st.button("Add", icon=":material/add:")

    dict2 = {"A": 0, "B": 0, "C": 0, "D": 0}

    def section_generating():
        try:
            for i in students:
                if i[2] in dict2:
                    dict2[i[2]] += 1
                else:
                    st.warning("Error Generated while Deciding the Section of Student")

        except Exception as e:
            
            st.error(f"Error Generated During The Process: {e}",icon=":material/error:")

        print(dict2.values())

        # Ensure dictionary is not empty before calling min()
        if dict2:
            min_value = min(dict2.values())
            return next((key for key, value in dict2.items() if value == min_value), None)
        else:
            return None

    if a:
        num = students[-1][4]  # Assuming student ID is at index 4
        new = str(num[-2]) + str(num[-1])  # Extract last two digits
        new2 = int(new) + 1  # Increment student number

       
       

        section = section_generating() 
         
        # Call function 
        try:

            students.append((name, str(class_new), section, transport, f"S0{new2}", a_num, "NA", "NhA", f_name, m_name))
            file.close()
            if section and a_num and f_name and m_name:
                st.success("Student Has Been Added Successfully", icon=":material/done_outline:")
            else:
                st.error("Please Add The Student Details",icon=":material/error:")
        except Exception as e:
            st.error("Error Is Being Generated While Adding Student: {e}",icon=":material/error:")
