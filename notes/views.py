from django.shortcuts import render
from notes.models import Note
# Create your views here.

def notes_list(request):
  notes = Note.objects.all()
  return render(request, "notes/notes_list.html", {'notes':notes})

def note_details(request, pk):
  note = Note.objects.get(pk=pk)
  return render(request, "notes/notes_details.html", {'notes':note})

