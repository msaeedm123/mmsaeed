from django.urls import path ,re_path
from . import views

urlpatterns = [
    re_path(r'^submit/expense/$', views.submit_expose, name='submit_expose'),
    re_path(r'^submit/income/$', views.submit_income, name='submit_income')
]
