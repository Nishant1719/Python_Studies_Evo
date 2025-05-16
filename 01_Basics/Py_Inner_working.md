# Python inner working 

- # Python is an Interpreted language 
    - As the PVM iterates continuesly (PVM Runtime Engine)
        - As soon as the byte code or any code is feeded to the PVM it iterates through the code and executes it.
        - As it interpretes line by line code
        - Python code can be directly feeded

- # python hello_world.py 
    - code ==> byte code (mostly hidden) (.pyc file) ==> PythonVM 

    - 1: Compile down (Intermeatary step) to Byte Code 
    - Low level code (Not Machine Code) & platform independent

    - # Byte Code:
        - Runs faster
        - .pyc -> Compiled python (frozen binaries)
        - __pycache__:
            - source change & python version
                - hello_world.cpython-313.pyc
            - Works only for imported files
            - not for top level files

- # PVM (Python Virtual Machine): Runtime Engine
    - This software is running a loop as soon as any files are sourced/feed it runs the code.
    - Also Known as Python Interpreter

- # Byte Code is not Machine Code
    - Python specifice Interpretation
    - cpython (standard Implementation),jythin,Iron Python, Stackless,PyPy 