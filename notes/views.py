from django.shortcuts import render
from notes.data import NOTES
# Create your views here.

def notes_list(request):
  return render(request, "notes/notes_list.html", {'notes':NOTES})

def note_details(request, id):
  note = NOTES[id]
  return render(request, "notes/notes_details.html", {'notes':note})

