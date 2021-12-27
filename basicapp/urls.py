from django.urls import path
from basicapp import views

#Template Tagging
app_name = 'basicapp'
urlpatterns = [
    path('basicapp/',views.basicapp,name='base'),
    path('',views.index,name='index'),
    path('relative/',views.relative,name='relative')
]
