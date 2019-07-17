from django.shortcuts import render
from emenu.models import *
from django.db.models import F
from django.db.models import Count
from django.core.paginator import Paginator
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from django.views.decorators.cache import cache_page
import time

ENTRIES_PER_PAGE = 8
CACHE_TTL = 60 * 15

@cache_page(CACHE_TTL)
@api_view(['GET', 'POST'])
def get_menu(request):
    data = get_serialized_menu()
    return Response(status=200,data=data)

@cache_page(CACHE_TTL)
@api_view(['GET', 'POST'])
def get_menu_detail(request):
    post_data = request.POST.dict()
    id = post_data['id']
    dishes = Dish.objects.filter(menu_id=id)\
        .values().order_by('id')
    dishes_data = DishSerializer(dishes, many=True).data
    return Response(status=200,data=dishes_data)



def main_page(request):
    menu_response = get_menu(request)
    context = {
        'menu_template': 'emenu/menu.html',
        'entries_per_page': ENTRIES_PER_PAGE,
    }
    #print('\n context: {}'.format(context))
    response = render(
        request,
        'emenu/main_page.html',
        context
    )
    return response

def get_serialized_menu():
    menus = Menu.objects\
        .annotate(num_dishes=Count('dishes__id'))\
        .order_by('id').values()
    menus = [menu for menu in menus if menu['num_dishes']>0]
    menus_serialized = MenuSerializer(menus, many=True).data
    return menus_serialized
