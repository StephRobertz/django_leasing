from django.urls import path

from app.views import landingview
from .views import landingview, locationlistview, carlistview, customerlistview, addlocation
from .views import confirmdeletelocation, edit_location_get, edit_location_post
from .views import addcar, deletecar, confirmdeletecar, searchcars, addcust, deletecust
from .views import confirmdeletecustomer, deletelocation, locations_filtered

urlpatterns = [
    path('', landingview),

    # Location url´s
    path('locations/', locationlistview),
    path('add-location/', addlocation),
    path('delete-location/<int:id>/', deletelocation),
    path('confirm-delete-location/<int:id>/', confirmdeletelocation),
    path('locations-by-car/<int:id>/', locations_filtered),
    path('edit-location-get/<int:id>/', edit_location_get),
    path('edit-location-post/<int:id>/', edit_location_post),

    # Car url´s
    path('cars/', carlistview),
    path('add-car/', addcar),
    path('delete-car/<int:id>/', deletecar),
    path('confirm-delete-car/<int:id>/', confirmdeletecar),
    path('search-cars/', searchcars),

    # Customer url´s
    path('customers/', customerlistview),
    path('add-customer/', addcust),
    path('delete-customer/<int:id>/', deletecust),
    path('confirm-delete-customer/<int:id>/', confirmdeletecustomer),
    # path('search-customer/', searchcustomers),
]
