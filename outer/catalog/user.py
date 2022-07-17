from django import shortcuts
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
# from django.contrib.auth.models import User
from catalog.models import UserProfile
from django.shortcuts import get_object_or_404


class UserCreateView(LoginRequiredMixin, generic.edit.CreateView):
    ''' sobreescribe el  método form_valid agregando un paso más a la validación del form,
    que es setearle el usuario que hace el request '''

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(UserCreateView, self).form_valid(form)


class UserUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    def get_queryset(self):
        ''' esto es para cuando un usuario o owner tiene muchas cosas que puede editar,
        en este caso es innecesario ya que es una relación uno a uno, pero igual añade
        seguridad y robustez'''
        qs = super(UserUpdateView, self).get_queryset()
        return qs.filter(user=self.request.user)

    def get_object(self):
        ''' esto hace que no haga falta pasar el slug por la url, ocultando información sensible
        a los usuarios, de lo contrario podrían intentar acceder a la página de edit profile de otro
        usuario, lo que sobrecargaría el servidor y además comprometería la seguridad, aunque reescribiendo
        el get queryset ya no podrían editarlo esto es lo óptimo'''
        return get_object_or_404(UserProfile, slug=self.request.user.username)
