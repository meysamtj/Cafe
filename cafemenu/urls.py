from django.urls import path
from .views import HomePage, Contact, CategoryView, CategoryDetailView, ItemsView, ItemsDetailView, item_search
app_name = 'cafemenu'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('contact/', Contact.as_view(), name='contact'),
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('all-items/', ItemsView.as_view(), name='all_items'),
    path('items/<slug:slug>/', ItemsDetailView.as_view(), name='item_detail'),
    path('search/', item_search, name='item_search'),
]
