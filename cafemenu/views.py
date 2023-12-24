from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, TemplateView
from .models import Category, Image, MenuItem
from cart.forms import AddToCartProductForm
from django.db.models import Q, F
# Create your views here.

# class HomePage(TemplateView):
#     template_name = 'cafemenu/main_page.html'
    
class HomePage(ListView):
    model = MenuItem
    template_name = 'cafemenu/main_page.html'
    context_object_name = 'items'
    queryset = MenuItem.objects.prefetch_related('image').order_by('id')[:6]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def item_search(request):
    search_query = request.GET.get('search')
    search = MenuItem.objects.filter(Q(item_name__icontains=search_query) | Q(description__icontains=search_query) | Q(category__category_name__icontains=search_query))
    return render(request, 'cafemenu/search.html', {'searchs': search})

    
class Contact(TemplateView):
    template_name = 'cafemenu/contact.html'

class CategoryView(ListView):
    model = Category
    template_name = 'cafemenu/catrgory.html'
    context_object_name = 'category'
    queryset = Category.objects.all()

class CategoryDetailView(ListView):
    model = MenuItem
    template_name = 'cafemenu/menuitem_list.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        return MenuItem.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
    
class ItemsView(ListView):
    model = MenuItem
    template_name = 'cafemenu/items_list.html'
    context_object_name = 'items'
    queryset = MenuItem.objects.prefetch_related('image')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    

class ItemsDetailView(DetailView):
    model = MenuItem
    template_name = 'cafemenu/item_detail_list.html'
    context_object_name = 'details'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['item_name'] = self.object
        description_lines = self.object.description.splitlines()
        context['description_lines'] = description_lines
        context['item_images'] = self.object.image.all()
        context['similar_item'] = MenuItem.objects.filter(category = self.object.category)
        context['add_to_cart_form'] = AddToCartProductForm()
        print(context['similar_item'])
        return context


# def home_page(request):
#     return render(request, 'cafemenu/main_page.html')

# def contact(request):
#     return render(request, 'cafemenu/contact.html')