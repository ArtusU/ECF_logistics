import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
	recipient__surname = django_filters.CharFilter(lookup_expr='icontains')
	referrer__surname = django_filters.CharFilter(lookup_expr='icontains')
	referrer__institution = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Order
		fields = ['recipient__surname', 'referrer__surname', 'referrer__institution', 'product', 'delivery_day', 'run', 'status']
		
