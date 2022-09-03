import email
from turtle import setundobuffer
from django.shortcuts import render
#from account.models import Account


def home(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/home.html', context)

def what_we_do(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/what_we_do.html', context)

def industries(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/industries.html', context)

def hospitality(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/hospitality.html', context)

    
def who_we_are(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/who_we_are.html', context)
    

def agriculture(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/agriculture.html', context)
    
def food(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/food.html', context)
    
def logistics(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/logistics.html', context)

def manufacturing(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/manufacturing.html', context)
    
def medical(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/medical.html', context)

def pharmaceutical(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/pharmaceutical.html', context)

def retail(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/retail.html', context)

def supply_chain(request):
    user = request.user
    hello = 'Hello'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/supply_chain.html', context)
    


