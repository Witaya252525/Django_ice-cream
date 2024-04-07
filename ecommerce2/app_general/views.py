from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse ("จันทร์ไรเดอร์")


def home(request):
    return render(request,'app_general/home.html')


def about(request):
    return HttpResponse ("เกี่ยวกับเรา")