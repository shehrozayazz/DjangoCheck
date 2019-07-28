from django.shortcuts import render,redirect
from .models import Destination

# Create your views here.

def showProduct(request,id):
    dest=Destination.objects.get(id=id)
    return render(request = request,template_name="products.html", context = {"dest":dest})
 

    # if dest.exists():
	#     return render(request = request,template_name="products.html", context = {"dest":dest})
    # else:
    #     redirect('/')



def index(request):

    dests=Destination.objects.all()
    
    return render(request,'index.html',{'dests':dests})