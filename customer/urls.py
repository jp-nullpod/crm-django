from django.urls import path
from . import views

app_name = 'qbfront'
urlpatterns = [
    # all experimental URLs here
    path("", views.customer_list, name="customer_list"),
    path("get/", views.get_list, name="get_list")
]