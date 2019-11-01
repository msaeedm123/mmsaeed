from django.shortcuts import render
from django.http import JsonResponse
import json
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from .models import User, Token, Expense, Income
from datetime import datetime
# Create your views here.
@csrf_exempt
def submit_expose(request):

    """user submit an expense"""
    print('we are here')
    # TODO: validate data, user might be fake, ...
    now = datetime.now()
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST['date']:
        date = datetime.now()
    Expense.objects.create(user=this_user, text=request.POST['text'],
                           amount=request.POST['amount'], date=date)
    print(this_user)
    print(request.POST)
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    """user submit an income"""
    print('we are here')
    # TODO: validate data, user might be fake, ...

    this_token1 = request.POST.get('token')
    this_user = User.objects.filter(token__token=this_token1).get()
    date_income = request.POST.get('date', datetime.now())
    Income.objects.create(user=this_user, text=request.POST['text'],
                          amount=request.POST['amount'], date=date_income)
    print(this_user)
    print(request.POST)
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)