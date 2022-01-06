"""
Serializers file.
This will convert instances of our model to JSON, so the Front-End can interact
with the received data.

"""

from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    '''
    Clase para serializar los modelos a formato Json.
    '''
    class Meta:
        '''
        Receive the model and the fields that are gonna be serialized.
        '''
        model = Todo
        fields = ('id', 'title', 'description', 'completed')



