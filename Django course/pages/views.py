from django.shortcuts import render
from django.http import HttpResponse

# Adding templates to be rendered when page is accessed.
def index(request):     
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')