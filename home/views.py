from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


from django.shortcuts import redirect

# def hello(request):
#      return HttpResponse("Hello")

class SignupView(CreateView):
     form_class = UserCreationForm
     template_name = 'home/register.html'
     # success_url = '/smart/notes'
     success_url = '/'
     


     def get(self, request, *args,**kwargs):
          if self.request.user.is_authenticated:
               return redirect('notes.list')
          return super().get(request,*args,**kwargs)

class LogoutInterfaceView(LogoutView):
     template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
     template_name = 'home/login.html'
     

# class LoginInterView(LoginView):
#      template_name = 'home/login.html'

class HomeView(TemplateView):
     template_name = 'home/home.html'
     extra_context = {"today": datetime.today()}
     

# def hello(request):
#      return render(request, "home/home.html", {"today": datetime.today()})

# @login_required(login_url="/login")
# def authorize(request):
#      return render (request, "home/login.html", {})


# @login_required(login_url="/admin")
# def authorize(request):
#      return render (request, "home/authorize.html", {})

