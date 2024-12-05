from django.urls import path
from . import views


urlpatterns = [
    path('submit_data', views.submit_data, name='submit_data'),
    path('', views.show_form, name='show_form'),
    path('success/', views.success_page, name='success_page'),
]