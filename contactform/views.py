from django.shortcuts import render,HttpResponse


#views
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        comment = request.POST['comment']
        print(name, email, phone,comment)



