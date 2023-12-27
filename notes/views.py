from django.shortcuts import render,redirect
from django.http.response import HttpResponseRedirect
from django.http import Http404
# from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.urls import reverse_lazy
from .models import Note
from .forms import NotesForm
# Create your views here.

class NoteDeleteView(DeleteView):
     model = Note
     success_url = '/smart/notes'
     template_name = 'notes/note_delete.html'


class NoteUpdateView(UpdateView):
     model = Note
     form_class = NotesForm
     # fields = ["title","text"]
     success_url = '/smart/notes'

class NoteListView(LoginRequiredMixin,ListView):
     model = Note
     context_object_name = "notes"
     template_name = "notes/notes_list.html"
     # login_url = '/admin'

class NoteDetailView(DetailView):
     model = Note
     context_object_name = "note"
     template_name = "notes/detail.html"



class NoteCreateView(CreateView):
     model = Note
     form_class = NotesForm
     # fields = ["title","text"]
     success_url = '/smart/notes'
     login_url = '/admin'

     def form_valid(self,form):
          self.object = form.save(commit=False)
          self.object.user = self.request.user
          self.object.save()
          return HttpResponseRedirect(self.get_success_url())





    

# other classes & functions

# def list(request):
#      notes = Note.objects.all()
#      return render(request, "notes/notes_list.html",{"notes":notes})

# def single_note(request, pk):
#      try :
#           note = Note.objects.get(pk=pk)
#      except Note.DoesNotExist:
#           raise Http404("The page does not exist")
#      return render (request, "notes/detail.html",{"note":note})
     
