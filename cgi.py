#!/usr/local/bin/python3.6
print("Content-Type: text/html")    
print()                             
 
import cgi,cgitb
cgitb.enable() #for debugging

print "<TITLE>CGI script output</TITLE>"
print "<H1>This is my first CGI script</H1>"
print "Hello, world!"

"""	
form = cgi.FieldStorage()

print("Content-Type: text/html") 
print()   
print "<p>"+ str(form) +"</p>"

print (form.keys())"""

