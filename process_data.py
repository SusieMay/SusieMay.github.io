#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()
selected_options = form.getlist('selected_options')

print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<title>Selected Options</title>")
print("</head>")
print("<body>")
print("<h1>Selected Options:</h1>")
print("<ul>")
for option in selected_options:
    print(f"<li>{option}</li>")
print("</ul>")
print("</body>")
print("</html>")