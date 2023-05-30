from django.urls import path
from .views import *

app_name = 'login'

urlpatterns = [
    path('', login_view, name='login'),
]
