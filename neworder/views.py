from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import get_object_or_404
from .models import *
from django.http import HttpResponse
import uuid
import json


class ItemView(APIView):
    permission_classes = (AllowAny,)
    # Get Items

    def get(self, request):
        return Response(
            {

                'pk': item.pk,
                'name': item.name,
                'price': item.price,
                'total_price': item.total_price,
                'subitems': [
                    {
                        'name': subitem.name,
                        'price': subitem.price,
                        'quantity': subitem.quantity
                    }
                    for subitem in item.subitems.all()]
            }

            for item in Items.objects.all())
    # Post New Item

    def post(self, request):
        item = Items()
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.total_price = request.POST.get('total_price')
        subs = request.POST.get('subitems')
        for i in subs:
            subitem = SubItems()
            subitem.name = i['name']
            subitem.price = i['price']
            subitem.quantity = i['quantity']
            item.subitems.add(subitem)
            subitem.save()
        item.save()
        return Response({})

        # Edit Existing Item
    def put(self, request):
        item = get_object_or_404(Items, pk=request.POST.get('pk'))
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.total_price = request.POST.get('total_price')
        subs = request.POST.get('subitems')
        for i in subs:
            subitem = SubItems()
            subitem.name = i['name']
            subitem.price = i['price']
            subitem.quantity = i['quantity']
            item.subitems.add(subitem)
            subitem.save()
        item.save()

        return Response({})
    # Delete Item

    def delete(self, request):
        item = get_object_or_404(Items, pk=request.POST.get('pk'))
        item.delete()
        return Response({})


class OrderView(APIView):
    permission_classes = (AllowAny,)
    # View Order

    def get(self, request):
        return Response(

            {
                'invoice_no': order.invoice_no,
                'ordered_items': [
                    {
                        'name': item.item.name,
                        'price': item.item.price,
                        'total_price': item.total_price,
                        'subitems': [
                            {
                                'name': subitem.name,
                                'price': subitem.price,
                                'quantity': subitem.quantity
                            }
                            for subitem in item.item.subitems.all()],
                        'session': order.session,
                        'total': order.total,
                        'paid_amount': order.paid_amount,
                        'paid': order.paid,
                        'returned_vessel': order.returned_vessel,
                        'balance': order.balance,
                        'date_placed': order.date_placed,
                        'date_of_delivery': order.date_of_delivery


                    }
                    for item in order.ordered_items.all()]

            }
            for order in Order.objects.all())
    # Place New Order

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
        items = list(request.POST.get('items'))
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
    # Edit Order

    def put(self, request):
        order = get_object_or_404(
            Order, invoice_no=request.POST.get('invoice_no'))
        customer = CustomerDetails()
        customer.u_id = uuid.uuid4()
        customer.phone_number = request.POST.get('phoneNum')
        customer.email = request.POST.get('email')
        customer.address = request.POST.get('address')
        customer.save()
        order.customer = customer
        items = list(request.POST.get('items'))
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
    # Delete Order

    def delete(self, request):
        order = get_object_or_404(
            Order, invoice_no=request.POST.get('invoice_no'))
        order.delete()
        return Response({})


class VesselView(APIView):
    # Get Vessels
    def get(self, request):
        return Response(

            {
                'u_id': item.u_id,
                'name': item.name
            }
            for item in Vessels.objects.all())

    # Add new Vessels
    def post(self, request):
        vessel = Vessels()
        vessel.name = request.POST.get('name')
        vessel.save()
        return Response({})
    # Edit Vessel

    def put(self, request):
        vessel = get_object_or_404(Vessels, u_id=request.POST.get('u_id'))
        vessel.name = request.POST.get('name')
        vessel.save()
        return Response({})
    # Delete Vessel

    def delete(self, request):
        vessel = get_object_or_404(Vessels, u_id=request.POST.get('u_id'))
        vessel.delete()
        return Response({})


class CustomerSearchView(APIView):
    # Get Customers
    def get(self, request):
        customers = CustomerDetails.objects.all()
        return Response([

            {
                'u_id': customer.u_id,
                'name': customer.name,
                'phone_number': customer.phone_number,
                'email': customer.email,
                'address': customer.address


            }

        ]for customer in customers)
    # Add Customers

    def post(self, request):
        customer = CustomerDetails()
        customer.name = request.POST.get('name')
        customer.phone_number = request.POST.get('phone_number')
        customer.email = request.POST.get('email')
        customer.address = request.POST.get('address')
        customer.save()
        return Response({})
    # Edit Customers

    def put(self, request):
        customer = get_object_or_404(
            CustomerDetails, u_id=request.POST.get('u_id'))
        customer.name = request.POST.get('name')
        customer.phone_number = request.POST.get('phone_number')
        customer.email = request.POST.get('email')
        customer.address = request.POST.get('address')
        customer.save()
        return Response({})
    # Delete Customers

    def delete(self, request):
        customer = get_object_or_404(
            CustomerDetails, u_id=request.POST.get('u_id'))
        customer.delete()
        return Response({})
