from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello_world(request):
    my_dict = {'insert_me': "Hello this comes from the django tempalte tag defined in the view"}
    return render(request,'hello_app/index.html',context=my_dict)


def help(request):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(request,'hello_app/index.html',context=helpdict)