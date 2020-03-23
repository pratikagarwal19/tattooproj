from django.http import JsonResponse
from django.shortcuts import render
import datetime
from .connection import Connection
import json
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


# Create your views here.

def weekly(request):
    return render(request, '../Templates/index.html')


def get_artist(request):
    db = Connection.connect('cloud')

    collection = db["artist"]
    artists = collection.find()
    artists_array = []

    for artist in artists:
        id = str(artist["_id"])
        del artist["_id"]
        artist["_id"] = id
        artists_array.append(artist)

    return JsonResponse(artists_array, safe=False)


def get_appointments(request):
    db = Connection.connect('cloud')

    collection = db["appoinments"]
    appointments = collection.find()
    print(appointments)
    appointments_array = []

    for appointment in appointments:
        id = str(appointment["_id"])
        del appointment["_id"]
        appointment["_id"] = id
        appointments_array.append(appointment)

    return JsonResponse(appointments_array, safe=False)




