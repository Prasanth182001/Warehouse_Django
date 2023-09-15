from django.shortcuts import render,redirect
from App.models import table_p,table_l,table_t
from App.forms import p_form,l_form

def home(request):
    return render(request,'home.html')

def product(request):
    data = table_p.objects.all()
    return render (request,"product.html",{'data':data})

def add_p(request):
    form = p_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('PDT')
    return render (request,'add_product.html',{'form':form})

def edit_p(request,id):
    edit=table_p.objects.get(id=id)
    form = p_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('PDT')
    return render(request,"edit_product.html",{'edit':edit})
    

def delete_p(request,id):
    Del=table_p.objects.get(id=id)
    Del.delete()
    return redirect("PDT")


def Location(request):
    data = table_l.objects.all() 
    return render(request,"location.html",{'data':data})

def add_l(request):
    forml = l_form(request.POST)
    if forml.is_valid():
        forml.save()
        return redirect('LCT')
    return render(request,'add_location.html',{'form1':forml})

def edit_l(request,id):
    edit = table_l.objects.get(id=id)
    form = l_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect("LCT")
    return render(request,'edit_location.html',{'edit':edit})

def delet_l(request,id):
    Del = table_l.objects.get(id=id)
    Del.delete()
    return redirect("LCT")

def transfer(request):
    data = table_t.objects.all()
    return render(request,"transfer.html",{"data":data})

def add_t(request):
    
    return render(request,"add_transfer.html")