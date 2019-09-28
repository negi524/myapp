from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World. You're at the todo_list index.")


def detail(request, ticket_id):
    return HttpResponse("You're looking at the detail of %s." % ticket_id)
