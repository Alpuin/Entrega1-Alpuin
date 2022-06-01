from django.db import models


class Staff(models.Model):

    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    rank = models.IntegerField()
    since = models.DateField()
    email = models.EmailField()
    
    def __str__(self):
        return (f'Nombre: {self.name} {self.last_name} // Cargo: {self.position} // Rango: {self.rank} // Ingreso: {self.since} // Contacto: {self.email}')


class Project(models.Model):

    code = models.IntegerField()
    title = models.CharField(max_length=40)
    start = models.DateField()
    state = models.CharField(max_length=40)

    def __str__(self):
        return (f'Proyecto {self.title} ({self.code}) // Inicio: {self.start} // Estado: {self.state}')


class Product(models.Model):
    
    serial = models.IntegerField()
    product_name = models.CharField(max_length=40)
    availability = models.BooleanField()

    def __str__(self):
        availability = 'Si' if self.availability else 'No'
        return (f'Objeto: {self.product_name} // Serie: {self.serial} // Disponible: {availability}')