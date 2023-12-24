from django.contrib import admin
from orders.models import Order
from import_export import resources


# Register your models here.
class PostResourse(resources.ModelResource):
    class Meta:
        model = Order
        fields = ("user", "created_at","is_paid")
        export_order = ("user","created_at","is_paid")
