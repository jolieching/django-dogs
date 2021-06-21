# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.views import generic
from .models import Pets


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'pet_list'
    
    def get_queryset(self):
        """Return the all greetings."""
        return Pets.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'create.html'
    model = Pets
    fields = ['name', 'image']
    success_url = reverse_lazy('pets:index') # more robust than hardcoding to /greetings/; directs user to index view after creating a greeting

class UpdateView(generic.edit.UpdateView):
    template_name = 'update.html'
    model = Pets
    fields = ['name', 'image']
    success_url = reverse_lazy('pets:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'delete.html' # override default of greetings/greeting_confirm_delete.html
    model = Pets
    success_url = reverse_lazy('pets:index')
