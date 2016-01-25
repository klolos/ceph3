from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from . import utils
from .forms import CreateObjectForm, EditObjectForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'demo/index.html'

    def get_queryset(self):
        return [utils.test_function()]

def index(request):
    context = {
        'data': sorted(utils.get_object_list()),
        'title': 'Dashboard',
    }
    return render(request, 'demo/index.html', context)

def details(request, object_name):
    data = utils.get_data(object_name)
    context = {
        'title': object_name,
        'object_name': object_name,
        'data': data,
    }
    return render(request, 'demo/details.html', context)

def edit(request, object_name):
    data = utils.get_data(object_name)
    form = EditObjectForm(initial={'data': data})
    context = {
        'title': 'Edit ' + object_name,
        'object_name': object_name,
        'data': data,
        'form': form,
    }
    return render(request, 'demo/edit.html', context)

def store(request, object_name):
    if request.method != 'POST':
        return HttpResponseRedirect('/demo/')

    if not utils.is_valid_name(object_name):
        messages.add_message(request, messages.INFO,
            'Invalid object name. Only letters, numbers ' + \
            'and dashes are allowed.')
        return HttpResponseRedirect('/demo/')

    form = EditObjectForm(request.POST)
    if not form.is_valid():
        messages.add_message(request, messages.INFO,
                             'The data provided was invalid.')
        return HttpResponseRedirect('/demo/edit/%s/' % object_name)
        
    data = form.cleaned_data['data']
    utils.store_object(object_name, data)
    messages.add_message(request, messages.INFO, 
                         'Object stored successfully.')
    return HttpResponseRedirect('/demo/object/%s/' % object_name)

def delete(request, object_name):
    if request.method != 'POST':
        messages.add_message(request, messages.INFO,
            'It was not POST.')
        return HttpResponseRedirect('/demo/')

    if not utils.exists(object_name):
        messages.add_message(request, messages.INFO,
            'Object %s not found.' % object_name)
        return HttpResponseRedirect('/demo/')
    else:
        utils.delete_object(object_name)
        messages.add_message(request, messages.INFO,
            'Object %s deleted!' % object_name)
        return HttpResponseRedirect('/demo/')
        
def create(request):
    form = CreateObjectForm()
    context = {
        'title': 'Create New Object',
        'form': form,
    }
    return render(request, 'demo/create.html', context)

def store_new(request):
    if request.method != 'POST':
        return HttpResponseRedirect('/demo/')

    form = CreateObjectForm(request.POST)
    if not form.is_valid():
        messages.add_message(request, messages.INFO,
                             'The data provided was invalid.')
        return HttpResponseRedirect('/demo/create/')
        
    data = form.cleaned_data['data']
    object_name = form.cleaned_data['object_name']
    if not utils.is_valid_name(object_name):
        messages.add_message(request, messages.INFO,
            'Invalid object name. Only letters, numbers ' + \
            'and dashes are allowed.')
        return HttpResponseRedirect('/demo/create/')

    if utils.exists(object_name):
        messages.add_message(request, messages.INFO,
            'Object already exists!')
        return HttpResponseRedirect('/demo/create/')

    utils.store_object(object_name, data)
    messages.add_message(request, messages.INFO, 
                         'Object created successfully.')
    return HttpResponseRedirect('/demo/object/%s/' % object_name)

