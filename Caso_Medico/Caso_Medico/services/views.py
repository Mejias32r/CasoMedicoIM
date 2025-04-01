from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/starter.html')

def query(request):
    return render(request, 'query/query.html')
def personalized(request):
    return render(request, 'dashboard/personalized.html')