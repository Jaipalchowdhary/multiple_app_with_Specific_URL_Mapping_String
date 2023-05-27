app_name='something'
from django.urls import path
from app2.views import *

urlpatterns=[

    path('dhavan/',dhavan,name='dhavan'),
]