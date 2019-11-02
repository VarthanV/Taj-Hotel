from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import get_object_or_404
from .models import *
from django.http import HttpResponse
import uuid


class ItemManipulationView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        data = [
            {
                'name': "Biriyani",
                'price': 100,
                'subitems': [
                    {
                        'name': 'Raitha',
                        'price': 30,
                        'quantity': '100ml'
                    },
                    {
                        'name': "Kuruma",
                        'price': 40,
                        'quantity': '30ml'
                    }
                ]
            },
            {
                'name': "Parotta",
                'price': 20,
                'subitems': [
                    {
                        'name': 'Raitha',
                        'price': 10,
                        'quantity': '100ml'
                    },
                    {
                        'name': "Kuruma",
                        'price': 40,
                        'quantity': '30ml'
                    }
                ]
            },
            {
                'name': "Idli",
                'price': 50,
                'subitems': [
                    {
                        'name': 'Sambar',
                        'price': 30,
                        'quantity': '100ml'
                    },
                    {
                        'name': "Cocount Chutney",
                        'price': 40,
                        'quantity': '30ml'
                    },
                    {
                        'name': "Kaara Chutney",
                        "price": 60,
                        'quantity': "40ml"
                    }
                ]
            },

        ]
        return Response(data)

        def post(self, request):
            pass


class OrderView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return HttpResponse("Get not allowed")

    def post(self, request):
        order = Order()
        o.invoice_no = request.POST.get('invoiceNo')
        customer = CustomerDetails()
        customer.u_id = uuid.uuid4()
        customer.phone_number = request.POST.get('phoneNum')
        customer.email = request.POST.get('email')
        customer.address = request.POST.get('address')
        customer.save()
        order.customer = customer
        items = request.POST.get('items')
        for i in items:
            item = get_object_or_404(Items, name=i['name'])
            ordered_item = OrderItem()
            ordered_item.item = item
            ordered_item.quantity = request.POST.get('quantity')
            ordered_item.total_price = request.POST.get('totalPrice')
            order.ordered_items.add(ordered_item)
            ordered_item.save()
        order.adv = request.POST.get('adv')
        order.session = request.POST.get('session')
        order.total = request.POST.get('total')
        order.date_of_delivery = request.POST.get('deliveryDate')
        order.save()
        return Response()
