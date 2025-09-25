# Constants are usually represented in CAPITAL_LETTERS.
    # >>> import functions1
    # >>> dir(functions1)
    # ['FILENAME', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'get_todos', 'write_todos']
    # >>>


FILENAME="todos.txt"

def get_todos(filename=FILENAME):#--> Default Parameter
    """
    DOC STRING
    This function reads a file and returns the to-do items as list.
    :param filename:
    :return:
    """
    with open(filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filename=FILENAME):#--> Default parameter should be mentioned after non default parameter.
    """
    DOC STRING
    This function write the list into a file.
    :param todos_arg:
    :param filename:
    :return:
    """
    with open(filename, 'w') as file:  # ---> With context manager
        file.writelines(todos_arg)

# print("hello from outside")
if __name__ == "_main__":
        print("HELLO from inside")