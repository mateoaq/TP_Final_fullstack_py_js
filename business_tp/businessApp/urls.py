from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('businessApp/', include('businessApp.urls')),
    path('business/', views.business, name='business'),
]
