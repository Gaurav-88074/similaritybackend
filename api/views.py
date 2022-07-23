from pickletools import string1
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import spacy
nlp = spacy.load("en_core_web_lg")

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def greet(request):
    return HttpResponse("hello")

@api_view(["POST"])
def comparison(request):
    obj = request.data

    string1 = obj['string1']
    string2 = obj['string2']

    doc1 = nlp(string1)
    doc2 = nlp(string2)

    # dummy = [
    #     {
    #         "Name" : "Gaurav"
    #     },
    #     {
    #         "Name" : "Sufian"
    #     }
    # ]
    value = doc1.similarity(doc2)
    resObj = {
        "similarity" : value
    }
    return Response(resObj)
    # print("Comparison of similarity [0-1]")
    