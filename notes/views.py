from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/smart/notes/"
    template_name = "notes/notes_delete.html"


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm
    template_name = "notes/notes_form.html"


class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    template_name = "notes/notes_form.html"
    success_url = "/smart/notes"


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
