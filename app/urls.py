from django.urls import path
from . import views

# URLConf module
urlpatterns = [
    path('list/', views.get_items, name="list"),
    path('itemform/', views.add_item, name="itemform"),
    path('edititem/<str:pk>/', views.edit_item, name='edititem'),
    path('deleteitem/<str:pk>/', views.delete_item, name="deleteitem"),
    path('sortbyid/', views.sort_by_id, name="sortbyid"),
    path('sortbyname/', views.sort_by_name, name="sortbyname")
]