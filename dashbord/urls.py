from django.urls import path, include
from . import views

app_name = "home"
urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('chart/', views.ChartListView.as_view(), name='report'),
]
