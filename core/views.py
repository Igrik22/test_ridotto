from datetime import datetime, timedelta

from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from core.forms import CustomerForm, ShopInfoForm
from core.models import ShopInfo, Customer


class ShopInfoCreateView(CreateView):
    model = ShopInfo
    fields = '__all__'
    template_name = 'shopping_form.html'

    def post(self, request, *args, **kwargs):
        form = ShopInfoForm(request.POST)
        if form.is_valid():
            customer = form.save()
            customer.save()
        return render(request, 'shopping_form.html', {'form': form})


class CustomerCreateView(CreateView):
    model = Customer
    fields = ['first_name', 'last_name']
    template_name = 'customer_form.html'

    def post(self, request, *args, **kwargs):
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            customer.save()
        return render(request, 'customer_form.html', {'form': form})


class GeneralShopInfoView(ListView):
    model = ShopInfo
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_list = []
        thedate = datetime.now() - timedelta(hours=72)
        thetime = datetime.now() - timedelta(hours=1)
        for customer in Customer.objects.all():
            one_of_customer = customer.shopinfos.filter(purchase_date__gte=thedate).\
                filter(purchase_time__gte=thetime)
            if len(one_of_customer) > 0:
                customer_list.append(one_of_customer)
        context['number_of_buyers'] = len(customer_list)
        context['number_of_purchases'] = len(ShopInfo.objects.filter(purchase_date__gte=thedate).
                                             filter(purchase_time__gte=thetime))
        context['total_price'] = (ShopInfo.objects.filter(purchase_date__gte=thedate).
                                  filter(purchase_time__gte=thetime).aggregate(Sum('price')))['price__sum']
        return context
