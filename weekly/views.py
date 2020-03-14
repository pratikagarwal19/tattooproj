from django.shortcuts import render

# Create your views here.


def weekly(request):
    return render(request, '../Templates/weekly.html', {
        'customer': ["A", "B", "C", "D", "E", "F", "G"],
        'appointment': ["9:30 Am - 10:00 AM", "6:00 Pm - 6:30 PM", "11:30 Am 12:10 Am", "5:00 Pm - 7:00 Pm", "5:00 Pm",
                        "3:30 Pm - 4:20 Pm", "2:00 Pm - 3:30 Pm"],
        'artist': ["artist A", "artist B", "artist C", "artist D", "artist E", "artist F", "artist G"],
        'range1': range(00, 25, 1),
        'range2': range(00, 60, 15)
    })