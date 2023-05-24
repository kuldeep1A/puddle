from . import views
from django.urls import path

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.delete, name='edit'),
    path('new/', views.new, name='new')
]