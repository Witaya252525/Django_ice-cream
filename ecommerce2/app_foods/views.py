from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime

# Create your views here.

# def foods(request):
#     return HttpResponse ("อาหาร อร่อย   ส่งรวดเร็ว")


# def food(request,food_id):
#     return HttpResponse ("เมนู ID = "  + str(food_id))


all_foods = [

        {'id':1 ,'title':'Dark Chore  Premium' ,'price':44444499 ,'is_premium':True,'promotion_end_at' : datetime(2022,2,28) },
        {'id':2 ,'title':'Red spicy' ,'price':349 ,'is_premium':False ,'promotion_end_at' : datetime(2022,2,15)},
        {'id':3 ,'title':'Blue Glacier' ,'price':3444449 ,'is_premium':False ,'promotion_end_at' : datetime(2022,4,5)},

]





def foods(request):
    context = { 'foods': all_foods}
    return render(request,'app_foods/foods.html' ,context)

def about(request):
    return render(request,'app_foods/about.html')


def food(request ,food_id):
    one_food = None
    try:
        one_food = [f for f in all_foods if f['id'] == food_id][0]
    except IndexError :
        print('ไม่มีเทอ ไม่ม่เทอ')
    
    context = {'food': one_food }
    return render(request,'app_foods/food.html' , context )

