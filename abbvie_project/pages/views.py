from django.http.response import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.


def home(request):
    context = {
        'message': "Hello, AbbVie world",
        'title': "Welcome to the AbbVie Project"
    }
    return render_to_response("pages/home.html", context=context)

def wombats_view(request):
    context = {
        'title': "Wombats!",
        'message1': "I like wombats!",
        'message2': "they are cuddly",
    }
    return render_to_response("pages/generic.html", context=context, status=201)
