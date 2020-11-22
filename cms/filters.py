import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
	recipient__full_name = django_filters.CharFilter(lookup_expr='icontains')
	referrer__surname = django_filters.CharFilter(lookup_expr='icontains')
	referrer__institution = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Order
		fields = ['referrer__surname', 'referrer__institution', 'recipient__full_name', 'product', 'status', 'delivery_day', 'run' ]
		

class DriverOrderFilter(django_filters.FilterSet):
	class Meta:
		model = Order
		fields = ['delivery_day', 'run']
		
