'''
####### to install #################
# pip install streamlit            #
####### to run this program ########
# open cmd and type the line below #
# streamlit run school_db_app.py   #
####################################
'''
import streamlit as st
from database import Student, Product, engine
from sqlalchemy.orm import sessionmaker

def opendb():
    Session = sessionmaker(bind=engine)
    return Session()

def save_student(nm,kls):
    db = opendb()
    student = Student(name=nm,klass=kls)
    db.add(student)
    db.commit()
    db.close()

st.sidebar.title("Database demo 1")

oplist = ['Add Student','View Student']
choice = st.sidebar.selectbox('Select an Option',oplist)
if choice == oplist[0]:
    st.header("add a new student detail")
    f = st.form('add student')
    name = f.text_input('student name')
    klass = f.selectbox('student class',[1,2,3,4,5,6,7,8,9,10,11,12])
    btn = f.form_submit_button("save student data")
    if btn and name and klass:
        save_student(name,klass)
        st.success("form data saved")

elif choice == oplist[1]:
    st.header("view student details")
    db = opendb()
    students = db.query(Student).all()
    for std in students:
        st.markdown(f'''
        {std.name}
        {std.klass}
        ''')