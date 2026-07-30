import ollama

from ollama import chat
from ollama import ChatResponse
#from ollama import ChatResponse, chat



#print(ollama)
#print(dir(ollama))

# response: ChatResponse = chat(model='gemma3', messages=[
#   {
#     'role': 'user',
#     'content': 'Why is the sky blue?',
#   },
# ])
# print(response['message']['content'])
# #### or access fields directly from the response object
# print(response.message.content)


from ollama import chat

response = chat(
    model="gemma3",
    messages=[
        {
            "role": "user",
            "content": """
You are a quiz generator.

Generate exactly three questions about the document.

Return valid JSON only.

Document:

Python Library Reference
Release 2.1.1
Guido van Rossum
Fred L. Drake, Jr., editor
July 20, 2001
PythonLabs
E-mail: python-docs@python.org

Copyright c⃝ 2001 Python Software Foundation. All rights reserved.
Copyright c⃝ 2000 BeOpen.com. All rights reserved.
Copyright c⃝ 1995-2000 Corporation for National Research Initiatives. All rights reserved.
Copyright c⃝ 1991-1995 Stichting Mathematisch Centrum. All rights reserved.
See the end of this document for complete license and permissions information.

Abstract
Python is an extensible, interpreted, object-oriented programming language. It supports a wide range of applications,
from simple text processing scripts to interactive WWW browsers.
While the Python Reference Manual describes the exact syntax and semantics of the language, it does not describe
the standard library that is distributed with the language, and which greatly enhances its immediate usability. This
library contains built-in modules (written in C) that provide access to system functionality such as ﬁle I/O that would
otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized
solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to
encourage and enhance the portability of Python programs.
This library reference manual documents Python’s standard library, as well as many optional library modules (which
may or may not be available, depending on whether the underlying platform supports them and on the conﬁguration
choices made at compile time). It also documents the standard types of the language and its built-in functions and
exceptions, many of which are not or incompletely documented in the Reference Manual.
This manual assumes basic knowledge about the Python language. For an informal introduction to Python, see the
Python Tutorial; the Python Reference Manual remains the highest authority on syntactic and semantic questions.
Finally, the manual entitled Extending and Embedding the Python Interpreter describes how to add new extensions to
Python and how to embed it in other applications.
"""
        }
    ],
)

print(response.message.content)