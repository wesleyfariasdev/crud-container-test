from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.container.models import Container
from apps.container.forms import ContainerForm


def container_list(request):
    template_name = 'container/container.html'
    containers = Container.objects.all()
    return render(request, template_name, {'containers': containers})


class CreateContainer(CreateView):
    template_name = 'container/container_form.html'
    model = Container
    form_class = ContainerForm
    success_url = reverse_lazy('container:list')

    def form_valid(self, form):
        form.save()
        return super(CreateContainer, self).form_valid(form)


class UpdateContainer(UpdateView):
    template_name = 'container/container_form.html'
    model = Container
    form_class = ContainerForm
    success_url = reverse_lazy('container:list')

    def form_valid(self, form):
        form.save()
        return super(UpdateContainer, self).form_valid(form)


def delete_container(request, pk):
    container = Container.objects.get(pk=pk)
    container.delete()
    return redirect('container:list')
