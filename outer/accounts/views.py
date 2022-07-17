from hashlib import new
from multiprocessing import context
from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.views import View, generic
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CreateUserForm
from django.urls import reverse, reverse_lazy
from accounts.forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages

from catalog.models import UserProfile

# class SignUpView(generic.edit.CreateView):
#     template_name = 'accounts/signup.html'
#     form_class = CreateUserForm
#     success_url = reverse_lazy('login')
#     model = User
#     form_class = CreateUserForm


class SignUpView(View):
    form_class = CreateUserForm
    template_name = 'accounts/signup.html'

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            # DESCOMENTAR ESTAS DOS LINEAS
            # userprofile = UserProfile(user=user)
            # userprofile.save()
            new_user = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Welcome {new_user}!',
            )
            return HttpResponseRedirect(reverse_lazy('login'))

        # form['email'] = request.POST['email']
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def get(self, request):
        form = self.form_class()

        context = {
            'form': form,
        }

        return render(request, self.template_name, context)
