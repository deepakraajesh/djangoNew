from django.urls import path
from helpapp import views,forms

urlpatterns = [
    path('help/',views.help,name='help'),
    path('forms/',views.form_name_view,name='form_name')
]
