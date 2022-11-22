from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, View
from apps.livros.models import Orientador, Livro
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from apps.livros.form import OrientadorForm

class OrientadorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = OrientadorForm
    success_message = 'Orientador cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_orientadores")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Orientadores - Biblioteca'
        context['descricao'] = 'Cadastro de Orientador'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Orientador
    form_class = OrientadorForm
    success_message = 'Orientador atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_orientadores")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Orientadores - Biblioteca'
        context['descricao'] = 'Editar Orientador(a)'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Orientador
    success_message = 'Orientador excluído com sucesso!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar_orientadores")

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['titulo'] = 'Orientadores - Biblioteca'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(OrientadorDelete, self).delete(request, *args, **kwargs)

class OrientadorList(ListView):
    model = Orientador
    template_name = "cadastros/listas/orientadores.html"

class TccsPorOrientadorList(ListView):
    model = Livro
    template_name = "index.html"
    paginate_by = 6

    def get_queryset(self):
        nome = self.request.GET.get('nome')

        if nome:
            return Livro.objects.filter(orientador=Orientador.objects.get(pk=self.kwargs['orientador']), titulo__icontains=nome)
        else:
            return Livro.objects.filter(orientador=Orientador.objects.get(pk=self.kwargs['orientador']))
