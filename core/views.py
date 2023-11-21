<<<<<<< HEAD
=======
from django.shortcuts import render
>>>>>>> 7be700f87883979e0e370f0c07dbb6b8052f9dda
from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
<<<<<<< HEAD
    template_name = "core/home.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"Mi primer web playground"})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
=======
    template_name = "core/home.html" 

    def get(self, request, *args, **Kwargs):
        return render(request, self.template_name, {'title':"Mi Super Web Playground"})

    
class SamplePageView(TemplateView):
    template_name = "core/sample.html"  
>>>>>>> 7be700f87883979e0e370f0c07dbb6b8052f9dda
