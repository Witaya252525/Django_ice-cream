from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

# def foods(request):
#     return HttpResponse ("อาหาร อร่อย   ส่งรวดเร็ว")


# def food(request,food_id):
#     return HttpResponse ("เมนู ID = "  + str(food_id))


def foods(request):
    return render(request,'app_foods/foods.html')

def about(request):
    return render(request,'app_foods/about.html')


def food(request ,food_id):
    return render(request,'app_foods/food.html' , context = {"food_id" : food_id })

