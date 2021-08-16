from django.urls import path
from data import views

urlpatterns = [
    path('create/',views.CreateCustomerdata.as_view() ),
    path('get/',views.GetCustomerdata.as_view() ),
    path('delete/<customer_id>',views.DeleteCustomerdata.as_view() ),
]
