from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item


@login_required
def index(request):
    item =

