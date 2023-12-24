from django.test import TestCase
from django.urls import resolve, reverse
from cafemenu.views import HomePage, Contact, CategoryView, CategoryDetailView, ItemsView, ItemsDetailView


# Create your tests here.


class TestUrl(TestCase):
    def test_HomePage(self):
        url = reverse('cafemenu:home')
        self.assertEqual(resolve(url).func.view_class, HomePage)

    def test_Contact(self):
        url = reverse('cafemenu:contact')
        self.assertEqual(resolve(url).func.view_class, Contact)

    def test_CategoryView(self):
        url = reverse('cafemenu:category')
        self.assertEqual(resolve(url).func.view_class, CategoryView)

    #
    def test_CategoryDetailView(self):
        url = reverse('cafemenu:category-detail', args=('te',))
        self.assertEqual(resolve(url).func.view_class, CategoryDetailView)

    #
    def test_ItemsDetailView(self):
        url = reverse('cafemenu:item-detail', args=('te',))
        self.assertEqual(resolve(url).func.view_class, ItemsDetailView)
