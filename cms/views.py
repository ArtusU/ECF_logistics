from cms.decorators import unauthenticated_user
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Delivery_Address, Order, Recipient, Referrer
from .forms import OrderForm, CreateUserForm, ReferrerForm, RecipientForm, AddressForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only



@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for '+ username)
            return redirect("cms:login")
    
    context = {'form': form}
    return render(request, 'cms/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("cms:home")
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'cms/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('cms:login')


login_required(login_url='cms:login')
#@allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    orders = Order.objects.all()
    
    new_orders = Order.objects.all().count()
    monday_orders = Order.objects.filter(delivery_day='Monday').count()
    tuesday_orders = Order.objects.filter(delivery_day='Tuesday').count()
    wednesday_orders = Order.objects.filter(delivery_day='Wednesday').count()
    thursday_orders = Order.objects.filter(delivery_day='Thursday').count()
    friday_orders = Order.objects.filter(delivery_day='Friday').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs.order_by('-date_created')
    #orders = myFilter.qs.order_by('delivery_address__post_code')


    context = {
        'new_orders': new_orders,
        'orders': orders,
        'monday_orders': monday_orders,
        'tuesday_orders': tuesday_orders,
        'wednesday_orders': wednesday_orders,
        'thursday_orders': thursday_orders,
        'friday_orders': friday_orders,
        'myFilter': myFilter,
    }
    return render(request, 'cms/admin_pan.html', context)



login_required(login_url='cms:login')
@allowed_users(allowed_roles=['admin', 'referrer'])
def referrerView(request):
    orders = request.user.referrer.order_set.all()
    #referrer = Referrer.objects.get(user=request.user)
    context = {
        #'referrer': referrer,
        'orders': orders
    }
    return render(request, 'cms/referrer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['referrer'])
def referrerSettings(request):
	referrer = request.user.referrer
	form = ReferrerForm(instance=referrer)

	if request.method == 'POST':
		form = ReferrerForm(request.POST, instance=referrer)
		if form.is_valid():
			form.save()

	context = {
        'form':form
        }
	return render(request, 'cms/referrer_settings.html', context)



login_required(login_url='cms:login')
@allowed_users(allowed_roles=['admin', 'driver'])
def driverView(request):
    #orders = Order.objects.filter(status='Out for Delivery')
    orders = Order.objects.all().order_by('delivery_address__post_code')
    
    context = {'orders': orders}
    return render(request, 'cms/driver.html', context)



login_required(login_url='cms:login')
@allowed_users(allowed_roles=['admin', 'referrer', 'driver'])
def orderDetails(request, pk):
    order_details = Order.objects.get(id=pk)
    context = {
        'order_details': order_details
    }
    return render(request, 'cms/order_details.html', context)



login_required(login_url='cms:login')
@allowed_users(allowed_roles=['admin', 'referrer'])
def createOrder(request):
    ord_form = OrderForm()
    recipient_form = RecipientForm()
    address_form = AddressForm()

    if request.method == 'POST':
        recipient_form = RecipientForm(request.POST)
        address_form = AddressForm(request.POST)
        ord_form = OrderForm(request.POST)

        if recipient_form.is_valid() and address_form.is_valid() and ord_form.is_valid():
            
            #Recipient.objects.create(**recipient_form.cleaned_data)
            obj_recipient = recipient_form.save(commit=False)
            obj_recipient.refereed_by = request.user.referrer
            obj_recipient.save()

            obj_address = address_form.save(commit=False)
            obj_address.recipient = obj_recipient
            obj_address.save()
            

            obj_order = ord_form.save(commit=False)
            obj_order.referrer = request.user.referrer
            obj_order.recipient = obj_recipient
            obj_order.delivery_address = obj_address
            obj_order.save()
            
            return redirect('/')


    context = {
        'recipient_form': recipient_form,
        'address_form': address_form,
        'ord_form': ord_form,
        
    }
    return render(request, 'cms/order_form.html', context)


login_required(login_url='cms:login')
@allowed_users(allowed_roles=['admin', 'referrer', 'driver'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'cms/order_form.html', context)



login_required(login_url='cms:login')
@allowed_users(allowed_roles=['admin', 'referrer', 'driver'])
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')
	context = {'item':order}
	return render(request, 'cms/delete.html', context)



