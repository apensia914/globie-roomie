from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('<int:pk>', views.RoomDetail.as_view(), name='detail'), #12.0 
    path('search/', views.search, name='search') #13.0 
]

'''
#12.0 URL path: https://docs.djangoproject.com/en/3.1/ref/urls/#path 
'''