from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Ticket, Content


def index(request):
    all_ticket = Ticket.objects.all()
    context = {
        'ticket_name': all_ticket,
    }
    return render(request, 'todo_list/index.html', context)


def detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    context = {
        'ticket': ticket
    }
    return render(request, 'todo_list/detail.html', context)
