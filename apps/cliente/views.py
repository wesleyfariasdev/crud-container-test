from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.cliente.models import Client
from apps.cliente.forms import ClientForm
from apps.container.models import Container
from apps.movimentacao.models import Movement


def client_list(request):
    template_name = 'client/client.html'
    clients = Client.objects.all()
    return render(request, template_name, {'clients': clients})


class ClientCreate(CreateView):
    template_name = 'client/client_form.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:list')

    def form_valid(self, form):
        form.save()
        return super(ClientCreate, self).form_valid(form)


class ClientUpdate(UpdateView):
    template_name = 'client/client_form.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:list')

    def form_valid(self, form):
        form.save()
        return super(ClientUpdate, self).form_valid(form)


def delete_client(request, pk):
    client = Client.objects.get(pk=pk)
    client.delete()
    return redirect('client:list')


# Filtro
def search(request):
    template_name = 'client/client.html'
    if request.method == 'POST':
        searched = request.POST['searched']
        clients = Client.objects.filter(
            Q(name__icontains=searched) |
            Q(cnpj__icontains=searched) |
            Q(email__icontains=searched)
        )
        context = {
            'searched': searched,
            'clients': clients
        }
        return render(request, template_name, context)
    else:
        return render(request, template_name)


def report_client(request, pk):
    template_name = 'report/report.html'
    client_report = Client.objects.get(pk=pk)
    container = Container.objects.filter(client=pk)
    type_movement = Movement.objects.filter(container__client__exact=client_report)
    number_imports = Container.objects.filter(client=pk, category='Importação').count
    number_exports = Container.objects.filter(client=pk, category='Exportação').count

    context = {
        'container': container,
        'client_report': client_report,
        'type_movement': type_movement,
        'number_imports': number_imports,
        'number_exports': number_exports,
    }

    return render(request, template_name, context)
