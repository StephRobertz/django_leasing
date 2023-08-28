from django.db import models

class Location(models.Model):
    city = models.CharField(max_length = 50, default="")
    postalcode = models.CharField(max_length = 50, default="")
    country = models.CharField(max_length = 100, default= "Finland")
   
    # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa paremmin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.city} , {self.country}"
    
class Car(models.Model):
    carname= models.CharField(max_length = 50, default="")
    model = models.CharField(max_length = 50, default="")
    year = models.CharField(max_length = 4, default="")
    gear = models.CharField(max_length = 100, default= "")
    price = models.CharField(max_length = 50, default=" $ /day")
   
    # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa paremmin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.carname} , {self.price}"
    

class Customer(models.Model):
    customername = models.CharField(max_length = 20, default = "")
    adress = models.CharField(max_length = 50, default = "")
    phone = models.CharField(max_length=50, default= "")
    mail = models.CharField(max_length= 50, default = "@gmail.com")
    #car = models.ForeignKey(Car, on_delete=models.CASCADE)
     # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa hienommin,
     # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.customername} ,call mobile on {self.phone}"
