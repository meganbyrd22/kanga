from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def recipe1(request):
    data = {
        "name": "Spaghetti Bolognese",
        "image_url": "https://example.com/spaghetti.jpg",
        "instructions": "1. Cook the pasta. 2. Prepare the sauce. 3. Combine and serve."
    }
    return JsonResponse(data)

def recipe2(request):
    data = {
        "name": "Chicken Curry",
        "image_url": "https://example.com/chicken-curry.jpg",
        "instructions": "1. Cook the chicken. 2. Prepare the curry sauce. 3. Combine and serve."
    }
    return JsonResponse(data)
