from django.db import models

# Create your models here.

# Define how the `TO DO` items should be stored in the database

class Todo(models.Model):
    '''
    Class to define how the To do items are gonna be stored in the database
    '''
    # Three properties: Title, description and completed.
    title = models.CharField(max_length=120) # Máximo 120 chars
    description = models.TextField() # Texto para ingresar la descripción
    completed = models.BooleanField(default=False) # Definir si la tarea esta o no terminada.

    # Method overload. Que se va a imprimir cuando se llame
    def __str__(self):
        return self.title




