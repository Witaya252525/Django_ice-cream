from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse ("จันทร์ไรเดอร์")


def about(request):
    return HttpResponse ("เกี่ยวกับเรา")