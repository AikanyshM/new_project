from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('form/', views.form),
    path('inventories/', views.inventory_view, name="all_inventories"),
    path('inventories/filter/', views.filter_inventories),
    path('inventories/<int:id>/', views.detail_view),
    path('inventories/<int:id>/delete/', views.delete_view),
    path('create_invent/', views.create_view),
    path('inventories/<int:id>/update/', views.update_view),
    path('categories/<int:id>/', views.detail_view_category),
    path('categories/<int:id>/delete/', views.delete_view_category),
    path('create_category/', views.create_view_category),


]