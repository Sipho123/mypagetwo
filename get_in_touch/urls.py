from django.urls import path
from  . import views



urlpatterns = [
    path('get_in_touch/', views.get_in_touch, name='get_in_touch-view'),
    #path('send_email/', views.send_email, name='send_email-view'),
    path('consultation/', views.consultation, name='consultation-view'),

]
