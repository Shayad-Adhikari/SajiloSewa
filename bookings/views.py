from django.shortcuts import render

# Create your views here.

def order_list(request):
    return render(request, "#")

def order_detail(request, id):
    return render(request, "#", {"order_id": id})

def create_order(request):
    return render(request, "#")