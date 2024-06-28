from django.shortcuts import render
from django.http import HttpResponse
from django.views  import View
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Rating
# Create your views here.
class SimpleView(View):
    def get(self , request):
        return HttpResponse(' hello , world')
    
    
    
class RatingsListView(ListView):
    model = Rating
    paginate_by: int =2 
class RatingsDetailView(DetailView):
    model = Rating
    template_name = 'rating/detail.html'
    
    
    
   
    




# class SimpleFormView(View):
#     form_class = SimpleForm
#     initial={'foo':'initial value'}
#     template_name = 'form_template.html'
    
    
    
    
#     def get(self , request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request , self . template_name , {'form': form})