from django.shortcuts import render
from bakery.views import BuildableDetailView, BuildableListView

from .models import Film

# Create your views here.

class FilmListView(BuildableListView):
    queryset = Film.objects.all()
    model = Film