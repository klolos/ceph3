from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from . import utils
from .forms import CreateObjectForm, EditObjectForm


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

def update(request, object_name):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('demo:index'))

    if not utils.is_valid_name(object_name):
        messages.add_message(request, messages.INFO,
            'Invalid object name. Only letters, numbers ' + \
            'and dashes are allowed.')
        return HttpResponseRedirect(reverse('demo:index'))

    form = EditObjectForm(request.POST)
    if not form.is_valid():
        messages.add_message(request, messages.INFO,
                             'The data provided was invalid.')
        return HttpResponseRedirect(reverse('demo:edit', 
                                            args=(object_name,)))
        
    data = form.cleaned_data['data']
    utils.store_object(object_name, data)
    messages.add_message(request, messages.INFO, 
                         'Object stored successfully.')
    return HttpResponseRedirect(reverse('demo:details',
                                        args=(object_name,)))

def delete(request, object_name):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('demo:index'))

    if not utils.exists(object_name):
        messages.add_message(request, messages.INFO,
            'Object %s not found.' % object_name)
        return HttpResponseRedirect(reverse('demo:index'))
    else:
        utils.delete_object(object_name)
        messages.add_message(request, messages.INFO,
            'Object %s deleted!' % object_name)
        return HttpResponseRedirect(reverse('demo:index'))
        
def create(request):
    form = CreateObjectForm()
    context = {
        'title': 'Create New Object',
        'form': form,
    }
    return render(request, 'demo/create.html', context)

def store(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('demo:index'))

    form = CreateObjectForm(request.POST)
    if not form.is_valid():
        messages.add_message(request, messages.INFO,
                             'The data provided was invalid.')
        return HttpResponseRedirect(reverse('demo:create'))
        
    data = form.cleaned_data['data']
    object_name = form.cleaned_data['object_name']
    if not utils.is_valid_name(object_name):
        messages.add_message(request, messages.INFO,
            'Invalid object name. Only letters, numbers ' + \
            'and dashes are allowed.')
        return HttpResponseRedirect(reverse('demo:create'))

    if utils.exists(object_name):
        messages.add_message(request, messages.INFO,
            'Object already exists!')
        return HttpResponseRedirect(reverse('demo:create'))

    utils.store_object(object_name, data)
    messages.add_message(request, messages.INFO, 
                         'Object created successfully.')
    return HttpResponseRedirect(reverse('demo:details',
                                        args=(object_name,)))

