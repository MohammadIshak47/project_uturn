from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Album
from first_app.forms import MusicianForm,AlbumForm
from first_app import forms


# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'title':"Homepage", 'musician_list':musician_list}
    return render(request,'first_app/index.html',context=diction)
def album_list(request,artist_id):
    diction = {'title':"List of Albums"}
    return render(request,'first_app/album_list.html',context=diction)
def musician_form(request):
    form = forms.MusicianForm()
    if request.method == "POST":
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
    diction={'title':"Add Musician",'musician_form':form}
    return render(request,'first_app/musician_form.html',context=diction)
def album_form(request):
    form = forms.AlbumForm()
    if request.method == "POST":
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
    diction={'title':"Add Album",'album_form':form}
    return render(request,'first_app/album_form.html',context=diction)
