from django.shortcuts import render
import datetime

# Create your views here.


def weekly(request):
    x = datetime.datetime.now()
    week_dict = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
    week = [0]*7

    day = x.strftime("%a")
    date = int(x.strftime("%d"))

    k = week_dict[day]

    for i in range(0, 7):
        week[i] = date - (k-i)

    return render(request, '../Templates/weekly.html', {
        'week': week
    })
