from django.shortcuts import render, redirect
from django .views import View
from .models import *


class Index (View):
    def get (self, request, *args, **kwargs):
        return render(request, 'index.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        list1 = Shopping.objects.filter(category__name__contains='regular')
        list2 = Shopping.objects.filter(category__name__contains='urgent')

        context ={
            'list1': list1,
            'list2': list2,
        }
        return render(request, 'store.html',)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        location = request.POST.get('location')
        phone_number = request.POST.get('phone_number')

        order_items = {
            'items':[]
        }
        items = request.POST.getlist('items[]')
        for item in items:
            shopping = Shopping.objects.get(pk__contains=int(item))
            item_data ={
                'id':shopping.pk,
                'name':shopping.name,
                'price':shopping.price
            }
            order_items['item'].append(item_data)
            price = 0
            item_ids = []

        for item in order_items['items']:

            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            name=name,
            email=email,
            location=location,
            phone_number=phone_number
        )
        context = {
            'items': order_items['items'],

        }
        return redirect('checkout', pk=order.pk,)

