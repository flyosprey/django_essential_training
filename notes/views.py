from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

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

    def form_valid(self, form):
        # Here we create 'object' that equals forms data
        # Than to 'object' variable we create new attribute 'user'
        # That equals to our 'user'
        self.object = form.save(commit=False)  # To get form data and then fill a field that the form does not have
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


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
