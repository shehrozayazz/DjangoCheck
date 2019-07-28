from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
class CBview(TemplateView):
   template_name='index.html'

class Result(TemplateView):


   def get(self, request):
      val1=float(request.POST['num1'])
      val2=float(request.POST['num2'])
      v=val1+val2
      return render(request, "result.html",{'result':v})

