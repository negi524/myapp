from django.shortcuts import render
from django.http import HttpResponse

from .models import Ticket, Content


def index(request):
    all_ticket = Ticket.objects.all()
    context = {
        'ticket_name': all_ticket,
    }
    return render(request, 'todo_list/index.html', context)


def detail(request, ticket_id):
    return HttpResponse("You're looking at the detail of %s." % ticket_id)
