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
print "<!DOCTYPE html><html><head>"
#jquery library
print "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js\"></script>"
#script
print """<script >
var cnt=0;
var id1;
var id2;
function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("Text", ev.target.id);
}

function drop(ev) {
  var data = ev.dataTransfer.getData("Text");
  ev.target.appendChild(document.getElementById(data));
  ev.preventDefault();
}
$(document).ready(function() {

    $('#table tr td').click(function() {
        if(cnt==0){
            id1 = $(this).attr("id");
            $(this).css('border-color', 'lime');
            cnt++;
            alert("First card selected");
        }
        else if(cnt==1){
            if($(this).attr("id")==id1){
                $(this).css('border-color', 'black');
                id1=0;
                cnt--;
                alert("card un-selected")
            }
            else{
                id2 = $(this).attr("id");
                $(this).css('border-color', 'lime');
                cnt++;
                alert("Second card selected");
            }
        }
        else {
            if($(this).attr("id")==id1){
                $(this).css('border-color', 'black');
                id1=id2;
                id2=0;
                cnt--;
                alert("card un-selected");
            }
            else if($(this).attr("id")==id2){
                $(this).css('border-color', 'black');
                cnt--;
                id2=0;
                alert("card un-selected");
            }
        }
    });
});
    </script>"""

print """<style>
	table{border:2px solid black; }
    td{border:2px solid black; cursor:pointer; height:100px;}</style>"""
print "<title>Weekly</title></head>"
print "<body>"
print "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"

print "<form id=custdets action=custdets.py>"

#time column
print "<table id=table style=\" float: left; \"><tr><th>TIME</th><th>day1</th><th>day 2</th><th>day 3</th><th>day 4</th><th>day 5</th><th>day 6</th><th>day 7</th></tr>"

for h in range(00,25,1):
    for m in range(00,60,15):
        for n in customer:
            if((m+15)==60):
                print "<tr><td>"+str(h)+" : "+str(m)+" to "+str(h+1)+" : 0 </td>"
            else:
                print "<tr><td>"+str(h)+" : "+str(m)+"<br>to<br>"+str(h)+" : "+str(m+15)+"</td>" #End of first cell

            #week 1
            print "<td draggable=true ondragstart=drag(event) id=c"+str(h)+"><label> Customer:   </label> <label name=c>"+str(customer[n-1])+"</label><br>"
            print "<label> Apointment: </label> <label name=time >"+str(apointment[n-1])+"</label><br>"     #replace apointment with database value
            print "<label> Artist:     </label> <label name=artist >"+str(artist[n-1])+"</label><br>"		#replace artist with database value
            print "<a href=custdets.py >View_Details</a></td>"

            #week 2
            print "<td draggable=true ondragstart=drag(event) id=c"+str(h)+"><label> Customer:   </label> <label name=c>"+str(customer[n-1])+"</label><br>"
            print "<label> Apointment: </label> <label name=time >"+str(apointment[n-1])+"</label><br>"     #replace apointment with database value
            print "<label> Artist:     </label> <label name=artist >"+str(artist[n-1])+"</label><br>"		#replace artist with database value
            print "<a href=custdets.py >View_Details</a></td>"

            #week 3
            print "<td draggable=true ondragstart=drag(event) id=c"+str(h)+"><label> Customer:   </label> <label name=c>"+str(customer[n-1])+"</label><br>"
            print "<label> Apointment: </label> <label name=time >"+str(apointment[n-1])+"</label><br>"     #replace apointment with database value
            print "<label> Artist:     </label> <label name=artist >"+str(artist[n-1])+"</label><br>"		#replace artist with database value
            print "<a href=custdets.py >View_Details</a></td>"

            #week 4
            print "<td draggable=true ondragstart=drag(event) id=c"+str(h)+"><label> Customer:   </label> <label name=c>"+str(customer[n-1])+"</label><br>"
            print "<label> Apointment: </label> <label name=time >"+str(apointment[n-1])+"</label><br>"     #replace apointment with database value
            print "<label> Artist:     </label> <label name=artist >"+str(artist[n-1])+"</label><br>"		#replace artist with database value
            print "<a href=custdets.py >View_Details</a></td>"

            #week 5
            print "<td draggable=true ondragstart=drag(event) id=c"+str(h)+"><label> Customer:   </label> <label name=c>"+str(customer[n-1])+"</label><br>"
            print "<label> Apointment: </label> <label name=time >"+str(apointment[n-1])+"</label><br>"     #replace apointment with database value
            print "<label> Artist:     </label> <label name=artist >"+str(artist[n-1])+"</label><br>"		#replace artist with database value
            print "<a href=custdets.py >View_Details</a></td>"

            #week 6
            print "<td draggable=true ondragstart=drag(event) id=c1r"+str(h)+"><label> Customer:   </label> <label name=c>"+str(customer[n-1])+"</label><br>"
            print "<label> Apointment: </label> <label name=time >"+str(apointment[n-1])+"</label><br>"     #replace apointment with database value
            print "<label> Artist:     </label> <label name=artist >"+str(artist[n-1])+"</label><br>"		#replace artist with database value
            print "<a href=custdets.py >View_Details</a></td>"

            #week 7
            print "<td draggable=true ondragstart=drag(event) id=c"+str(h)+"><label> Customer:   </label> <label name=c>"+str(customer[n-1])+"</label><br>"
            print "<label> Apointment: </label> <label name=time >"+str(apointment[n-1])+"</label><br>"     #replace apointment with database value
            print "<label> Artist:     </label> <label name=artist >"+str(artist[n-1])+"</label><br>"		#replace artist with database value
            print "<a href=custdets.py >View_Details</a></td>"

            print "</tr>" #End of row
print "</table>"



print "</form>"

print "</body></html>"
