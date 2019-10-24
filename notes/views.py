from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Note
from notes.forms import NoteForm
# Create your views here.


def notes_list(request):
    notes = Note.objects.all()
    return render(request, "notes/notes_list.html", {'notes': notes})


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, "notes/notes_details.html", {'note': note})


def create_note(request):
    if request.method == "POST":  #form was submitted
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect(to='notes_list')
    else:
        form = NoteForm()

    return render(request, "notes/create_note.html", {"form": form})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            note = form.save()
            return redirect(to='notes_details', pk=note.id)
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/edit_note.html", {
        "note": note,
        "form": form,
    })


def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    note.delete()
    notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {"notes": notes})
