from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.movimentacao.forms import MovementForm
from apps.movimentacao.models import Movement


def movement_list(request):
    template_name = 'movement/movement.html'
    movements = Movement.objects.all()
    return render(request, template_name, {'movements': movements})


class MovementCreate(CreateView):
    template_name = 'movement/movement_form.html'
    model = Movement
    form_class = MovementForm
    success_url = reverse_lazy('movement:list')

    def form_valid(self, form):
        form.save()
        return super(MovementCreate, self).form_valid(form)


class MovementUpdate(UpdateView):
    template_name = 'movement/movement_form.html'
    model = Movement
    form_class = MovementForm
    success_url = reverse_lazy('movement:list')

    def form_valid(self, form):
        form.save()
        return super(MovementUpdate, self).form_valid(form)


def delete_movement(request, pk):
    movement = Movement.objects.get(pk=pk)
    movement.delete()
    return redirect('movement:list')
