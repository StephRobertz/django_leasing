from django.urls import path


from .views import locationlistview, carlistview, customerlistview, addlocation
from .views import confirmdeletelocation, edit_location_get, edit_location_post
from .views import addcar, deletecar, confirmdeletecar, searchcars, addcust, deletecust
from .views import confirmdeletecustomer, deletelocation, locations_filtered, edit_customer_get, edit_customer_post
from .views import edit_car_post, edit_car_get, searchlocations, loginview, login_action, logout_action

urlpatterns = [
    # path('', landingview),

    # Login & logout
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

    # Location url´s
    path('locations/', locationlistview),
    path('add-location/', addlocation),
    path('delete-location/<int:id>/', deletelocation),
    path('confirm-delete-location/<int:id>/', confirmdeletelocation),
    path('locations-by-car/<int:id>/', locations_filtered),
    path('edit-location-get/<int:id>/', edit_location_get),
    path('edit-location-post/<int:id>/', edit_location_post),
    path('search-locations/', searchlocations),

    # Car url´s
    path('cars/', carlistview),
    path('add-car/', addcar),
    path('delete-car/<int:id>/', deletecar),
    path('confirm-delete-car/<int:id>/', confirmdeletecar),
    path('search-cars/', searchcars),
    path('edit-car-get/<int:id>/', edit_car_get),
    path('edit-car-post/<int:id>/', edit_car_post),

    # Customer url´s
    path('customers/', customerlistview),
    path('add-customer/', addcust),
    path('delete-customer/<int:id>/', deletecust),
    path('confirm-delete-customer/<int:id>/', confirmdeletecustomer),
    path('edit-customer-get/<int:id>/', edit_customer_get),
    path('edit-customer-post/<int:id>/', edit_customer_post),
    # path('search-customer/', searchcustomers),
]
