from django.shortcuts import render


def weekly(request):
    return render(request, '../Templates/weekly.html')
