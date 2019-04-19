from django.http import HttpResponse
from django.shortcuts import render
import sqlite3

# Create your views here.
def index(request):
    print("kkkk")
    return HttpResponse("网页")

def test():
    print("test")

