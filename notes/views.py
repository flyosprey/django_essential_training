from django.views.generic import CreateView, ListView, DetailView

from .forms import NotesForm
from .models import Notes


class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    template_name = "notes/notes_form.html"
    success_url = "/smart/notes"


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
