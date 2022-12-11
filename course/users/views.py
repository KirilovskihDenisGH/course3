from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
# from .models import Personal_area

class Signup(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'


# class Personal(ListView):
#     model = Personal_area
#     template_name = 'personal_area.html'