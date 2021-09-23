from django import forms
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Details
#from .forms import CreateNewList


# Create your views here.


def index(request):
    #Getting data from the HTML and accepting
    if request.method == 'POST':
        #form = Details(request.POST) 
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        comment = request.POST['comment']
        
        #Creating the Object of record every time user clicks on 'Add Data'
        '''
        if form.isvalid():
            return redirect('/success/')
        '''  
        obj = Details()
        obj.name = name
        obj.email = email
        obj.phone = phone 
        obj.comment = comment
        obj.save()
        
    #Fetching the details and saving in an dictionary
    from django.core import serializers
    data = serializers.serialize("python",Details.objects.all())

    #Dictionary to store the data and send it back to HTML format
    context = {
        'data':data,
    }
    
    for row in Details.objects.all():
        if Details.objects.filter(phone=row.phone).count() > 1:
            row.delete()
        #return HttpResponseRedirect("/sample")
    '''
    if request.method == 'POST':
        myfunc()
    '''
        
    return render(request, 'contact_us.html', context) 
def self(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about_us.html')


def sample(request):
    return render(request, 'sample.html')

def myfunc():
    return HttpResponseRedirect('/sample')
