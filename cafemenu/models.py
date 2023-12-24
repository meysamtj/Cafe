from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    sub_image = models.ImageField('category_image', upload_to='category_img/', height_field=None, width_field=None,null=True,blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.category_name


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menuitem')
    item_name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    mojoudi = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    description = models.TextField(default="")
    main_image = models.ImageField('Menu_Item_Main_Image',  upload_to='menu_item_img/', height_field=None, width_field=None, null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item_name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.item_name}'


class Image(models.Model):

    sub_image = models.ImageField('Menu_Item_Image',  upload_to='menu_item_img/', height_field=None, width_field=None, null=True,blank=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='image')
    
    
# class ShoppingCart(models.Model):
#     item_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='shoppingcart')    # ask abolfazl
#     quantity = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add=True) # ask abolfazl
#     updated_at = models.DateTimeField(auto_now=True)    # ask abolfazl
#     total_price = models.PositiveIntegerField()