from django import forms
from .models import Note
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
     class Meta :
          model = Note
          fields = ('title','text')
          widgets = {
               "title":forms.TextInput(attrs={'class':'form-control my-2'}),
               "text":forms.Textarea(attrs={'class':'form-control mb-2 '})

          }
          labels = {
               "text":"Write your text"
          }
     # def clean_title(self):
     #      title = self.cleaned_data["title"]
          # if "Django" not in title:
          #      raise ValidationError("We only accept Django note")
          # return title


