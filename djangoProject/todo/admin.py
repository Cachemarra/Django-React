from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    #The touple must have the same fields than the one in models.
    list_display = ('title', 'description', 'completed')


# Registering the model.
admin.site.register(Todo, TodoAdmin)





