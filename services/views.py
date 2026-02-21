from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "#")

def gig_list(request):
    return render(request, "#")

def gig_detail(request, id):
    return render(request, "#", {"gig_id": id})

def create_gig(request):
    return render(request, "#")