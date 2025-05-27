import django_filters
from .models import Movimiento

class MovimientoFilter(django_filters.FilterSet):
    min_monto = django_filters.NumberFilter(field_name="monto", lookup_expr='gte')
    max_monto = django_filters.NumberFilter(field_name="monto", lookup_expr='lte')

    class Meta:
        model = Movimiento
        fields = ['tipo', 'categoria', 'cuenta', 'min_monto', 'max_monto']
