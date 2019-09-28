from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Ticket, Content


def index(request):
    all_ticket = Ticket.objects.all()
    template = loader.get_template('todo_list/index.html')
    context = {
        'ticket_name': all_ticket,
    }
    return HttpResponse(template.render(context, request))


def detail(request, ticket_id):
    return HttpResponse("You're looking at the detail of %s." % ticket_id)
