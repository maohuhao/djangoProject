from django.urls import path
from .views.login import *

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('send_email/', send_email, name='send_email'),
    path('index/', index, name='index'),
]