from django.urls import path, include
from Goods import views

urlpatterns = [
    path('', views.banner, name='banner'),
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
]