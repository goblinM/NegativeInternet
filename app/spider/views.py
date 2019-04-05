from django.http import HttpResponse
from django.shortcuts import render
import lxml
# Create your views here.
def index(request):
    print("hhhhhhhhh")
    return HttpResponse("爬取数据")