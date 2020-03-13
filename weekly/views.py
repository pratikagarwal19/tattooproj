from django.shortcuts import render
()

# Create your views here.

#!/usr/bin/env python
#above line is for python execution in apache remove when using in other environment

import cgi, cgitb      			#for processing form values

#dummy values below
 
customer = [1,2,3,4,5,6,7]
apointment = ["9:30 Am - 10:00 AM","6:00 Pm - 6:30 PM","11:30 Am 12:10 Am","5:00 Pm - 7:00 Pm","5:00 Pm","3:30 Pm - 4:20 Pm","2:00 Pm - 3:30 Pm"]
artist = ["artist A","artist B","artist C","artist D","artist E","artist F","artist G"]

cgitb.enable()
form = cgi.FieldStorage()

print "Content-type: text/html\n\n"
print "<html><head>"
print """<style>					#css-style
	table, th,td{border:3px solid black;}</style>"""
print "<title>Weekly</title></head>"
print "<body>"

print "<form id=custdets>" 



print "<table style=\" float: left; \"> <tr> <td><label>" +"day 1"+ "</label> </td> </tr> </td>"         #first column

for n in customer: #for id in customer column
    print "<div style =\" align-items: center; \" id=t2c"+str(n-1)+">"
    print "<tr><td><label> Customer:   </label> <label name=c>"+str(customer[n-1])+"</label><br>"		#replace customer with database value use where id= n
    print "<label> Apointment: </label> <label name=t>"+str(apointment[n-1])+"</label><br>"		#replace apointment with database value
    print "<label> Artist:     </label> <label name=a>"+str(artist[n-1])+"</label><br>"		#replace artist with database value
    print "<input type=submit value=View_Details></td></tr>"
    print "</div>"

print "</table>"

print "<table style=\" float: left; \"> <tr> <td><label>" +"day 2"+ "</label> </td> </tr> </td>"         #second column

for n in customer: #for id in customer column
    print "<div style =\" align-items: center; \" id=t2c"+str(n-1)+">"
    print "<tr><td><label> Customer:   </label> <label name=c>"+str(customer[n-1])+"</label><br>"		#replace customer with database value use where id= n
    print "<label> Apointment: </label> <label name=t>"+str(apointment[n-1])+"</label><br>"		#replace apointment with database value
    print "<label> Artist:     </label> <label name=a>"+str(artist[n-1])+"</label><br>"		#replace artist with database value
    print "<input type=submit value=View_Details></td></tr>"
    print "</div>"

print "</table>"

print "</form>"

print "</body></html>"
