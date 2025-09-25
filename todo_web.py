import streamlit as st
import functions1

todos = functions1.get_todos()

def addtodo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions1.write_todos(todos)

st.title("My ToDo Web App")
st.subheader("Testing sub header")
st.write("Testing normal text")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions1.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input("", placeholder="Add a new todo item..", on_change=addtodo, key="new_todo")

st.session_state