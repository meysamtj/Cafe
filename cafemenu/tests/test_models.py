from django.test import TestCase
from django.urls import resolve, reverse
from cafemenu.models import Category, MenuItem
from model_bakery import baker


class TestCategoryModel(TestCase):
    def test_model_str(self):
        category = baker.make(Category, category_name='hello')
        self.assertEqual(str(category), 'hello')
        self.assertTrue(category.slug, 'hello')


class TestMenuItemModel(TestCase):
    def test_model_str(self):
        menu_item = baker.make(MenuItem, item_name='hello')
        self.assertEqual(str(menu_item), 'hello')
        self.assertTrue(menu_item.slug, 'hello')

    # def test_model_save(self):
    #     menu_item = baker.make(MenuItem, slug='salam')
    #     self.assertEqual(str(menu_item), 'hello')
