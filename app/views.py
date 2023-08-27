from django.shortcuts import render, redirect
from .models import Location, Car, Customer

def landingview(request):
    return render(request, 'landingpage.html')

def locationlistview(request):
    return render(request, 'locationlist.html')

def carlistview(request):
    return render(request, 'carlist.html')

def customerlistview(request):
    return render(request, 'customerlist.html')



# Product view´s

def locationlistview(request):
    locationlist = Location.objects.all()
    context = {'locations': locationlist}
    return render (request,"locationlist.html",context)


def addlocation(request):
    a = request.POST['city']
    b = request.POST['postalcode']
    c = request.POST['country']
    e = request.POST['car']
    
    Location(city = a, postalcode = b, country = c, car = Car.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])


def confirmdeletelocation(request, id):
    location = Location.objects.get(id = id)
    context = {'location': location}
    return render (request,"confirmdelloc.html",context)


def deletelocation(request, id):
    Location.objects.get(id = id).delete()
    return redirect(locationlistview)


def edit_location_get(request, id):
        location = Location.objects.get(id = id)
        context = {'location': location}
        return render (request,"edit_location.html",context)


def edit_location_post(request, id):
        item = Location.objects.get(id = id)
        item.city = request.POST['city']
        item.postalcode = request.POST['postalcode']
        item.save()
        return redirect(locationlistview)

def locations_filtered(request, id):
    locationlist = Location.objects.all()
    filteredlocations = locationlist.filter(car = id)
    context = {'locations': filteredlocations}
    return render (request,"locationlist.html",context)


# Supplier view´s
def carlistview(request):
    carlist = Car.objects.all()
    context = {'cars': carlist}
    return render (request,"carlist.html",context)

def addcar(request):
    a = request.POST['carname']
    b = request.POST['model']
    c = request.POST['year']
    d = request.POST['gear']
    e = request.POST['price']
    f = request.POST['city']
    Car(carname = a, model = b, year = c, gear = d, price = e).save()
    return redirect(request.META['HTTP_REFERER'])
    

def confirmdeletecar(request, id):
    car = Car.objects.get(id = id)
    context = {'car': car}
    return render (request,"confirmdelcar.html",context)

def deletecar(request, id):
    Car.objects.get(id = id).delete()
    return redirect(carlistview)


def searchcars(request):
    search = request.POST['search']
    filtered = Car.objects.filter(carname__icontains=search)
    context = {'cars': filtered}
    return render (request,"carlist.html",context)


# Supplier view´s
def customerlistview(request):
    customerlist = Customer.objects.all()
    context = {'customers': customerlist}
    return render (request,"customerlist.html",context)

def addcust(request):
    a = request.POST['name']
    b = request.POST['adress']
    c = request.POST['phone']
    d = request.POST['mail']
    e = request.POST['car']
    Customer(name = a, adress = b, phone = c, mail = d, car = e).save()
    return redirect(request.META['HTTP_REFERER'])
    

def confirmdeletecustomer(request, id):
    customer = Customer.objects.get(id = id)
    context = {'customer': customer}
    return render (request,"confirmdelcust.html",context)


def deletecust(request, id):
    Customer.objects.get(id = id).delete()
    return redirect(customerlistview)