from django.shortcuts import render,redirect
from .form import studentform
from .models import student

# Create your views here.
def Navbar(request):
    template_name="navbar.html"
    return render(request,template_name)

def Data(request):
    data=student.objects.all()
    template_name="data.html"
    context={'data':data}
    return render(request,template_name,context)

def Form(request):
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("data")
    form=studentform()
    template_name="form.html"
    context={'form':form}
    return render(request,template_name,context)

def Delete(request,id):
    data=student.objects.get(id=id)
    data.delete()
    return redirect("data")

def Update(request,id):
    data=student.objects.get(id=id)
    if request.method=="POST":
        form=studentform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("data")
    form=studentform(instance=data)
    template_name="update.html"
    context={'form':form}
    return render(request,template_name,context)