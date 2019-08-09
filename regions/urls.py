from django.urls import path
from .views import list_regions, create_region, update_region, delete_region, create_commune, update_commune, delete_commune


urlpatterns = [
    path('', list_regions, name='list_regions'),
    path('new', create_region, name='create_region'),
    path('update/<int:id>/', update_region, name='update_region'),
    path('delete/<int:id>/', delete_region, name='delete_region'),
    path('new_commune', create_commune, name='create_commune'),
    path('update_commune/<int:id>/', update_commune, name='update_commune'),
    path('delete_commune/<int:id>/', delete_commune, name='delete_commune'),
]