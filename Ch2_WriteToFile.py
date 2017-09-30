my_variable = "<html><head><title>Look at this</title></head></body><h1>hello world</h1></body></html>"  # variable

my_html_file = open("/PythonMSK/my_html_file.html", "w")  # using open keyword, creating html file in PythonMSK dir
#  w = write

my_html_file.write(my_variable)  # variable.write(html content) ... aka write to an html file, contents in my_variable
