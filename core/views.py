from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm, LoginForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', dict(form=form))


def login(request):
    if request.method == 'GET':
        form = LoginForm(request.GET)
        if form.is_valid():
            return redirect('')
    form = LoginForm()
    return render(request, 'core/login.html', dict(form=form))