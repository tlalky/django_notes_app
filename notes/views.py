from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView, CreateView


from .models import Notes
from .forms import NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist!")
    return render(request, 'notes/notes_detail.html', {'note': note})
