import django_filters
from .models import Booking, Tour



class TourFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    start_date = django_filters.DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='end_date', lookup_expr='lte')
    place = django_filters.CharFilter(field_name='place', lookup_expr='icontains')

    class Meta:
        model = Tour
        fields = ['price', 'start_date', 'end_date', 'place']

    


    

