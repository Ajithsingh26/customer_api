from django.core import paginator
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .models import Customers
from .serializer import CustomerSerializer
from django.core.paginator import Paginator

class CreateCustomerdata(APIView):
    
    def post(self,request):
        try:
            data= request.data
            customer_name = (data.get("name"))
            customer_age = (data.get("age"))
         
            customer_new, created = Customers.objects.update_or_create(customer_name=customer_name,customer_age =customer_age
                                                                     )

            return Response(
                    status=status.HTTP_200_OK,
                    data={'data':"Created Successfully",
                    'status':status.HTTP_200_OK}
                )

        except Exception as e:
            print(str(e))
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error':str(e)}
            )

class GetCustomerdata(APIView):
    
    def get(self,request):
        try:
            customer_obj = Customers.objects.all()            
            paginator = Paginator(customer_obj,3)
            page = request.GET.get('pg')
            customer_obj = paginator.get_page(page)
            all_data = []
            for customer in customer_obj:
                customer_data = CustomerSerializer(instance=customer)
                all_data.append(customer_data.data)
               
            return Response(
                    status=status.HTTP_200_OK,
                    data= all_data
                )

        except Exception as e:
            print(str(e))
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error':str(e)}
            )

class DeleteCustomerdata(APIView):
    
    def delete(self,request, customer_id):
        try:
            #customer_data = Customers.objects.all()
            d_customer = Customers.objects.get(pk=customer_id)
            d_customer.delete()
            
            return Response(
                    status=status.HTTP_200_OK,
                    data= "successfullt deleted"
                )

        except Exception as e:
            print(str(e))
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error':str(e)}
                )



