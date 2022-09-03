from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name='home-view'),
    path('what_we_do/', views.what_we_do, name='what_we_do-view'),
    path('industries/', views.industries, name='industries-view'),
    #path('products/', views.products_view, name='products-view'),
    path('who_we_are/', views.who_we_are, name='who_we_are-view'),
    path('agriculture/', views.agriculture, name='agriculture-view'),
    path('hospitality/', views.hospitality, name='hospitality-view'),
    path('food/', views.food, name='food-view'),
    path('logistics/', views.logistics, name='logistics-view'),
    path('manufacturing/', views.manufacturing, name='manufacturing-view'),
    path('medical/', views.medical, name='medical-view'),
    path('pharmaceutical/', views.pharmaceutical, name='pharmaceutical-view'),
    path('retail/', views.retail, name='retail-view'),
    path('supply_chain/', views.supply_chain, name='supply_chain-view'),

]