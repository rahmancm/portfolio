from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from entry.models import entrie
from django.contrib import messages

def homeView(request):
    if request.method == 'POST':
           name=request.POST["name"]
           address=request.POST["address"]
           phone=request.POST["phone"]
           pincoe=request.POST["pincoe"]
           entries=entrie(name=name,address=address, phone=phone, pincoe=pincoe)
           if name is None or address is None or pincoe is None:
             return redirect('/')
           else:
             entries.save()
             print("User created")
             return redirect('/')
    blog_object= entrie.objects.all()
    return render(request,'index222.html',{'blog_object':blog_object})
def entries(request):

    return render(request,'index.html')
def contact(request):
    return render(request,'contactme.html')
