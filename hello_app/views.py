from django.shortcuts import render
from django.http import HttpResponse
from hello_app.models import Topic,Webpage,AccessRecord



# Create your views here.

def hello_world(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dic = {'access_records':webpages_list}
    return render(request,'hello_app/index.html',context=date_dic)
