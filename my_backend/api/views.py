from django.http import JsonResponse
from .models import Recipe

def recipe_list(request):
    
    if Recipe.objects.count() == 0:
        Recipe.objects.create(
            name="Spaghetti Bolognese",
            image_url="https://example.com/spaghetti.jpg",
            instructions="1. Cook the pasta. 2. Prepare the sauce. 3. Combine and serve."
        )
        Recipe.objects.create(
            name="Chicken Curry",
            image_url="https://example.com/chicken-curry.jpg",
            instructions="1. Cook the chicken. 2. Prepare the curry sauce. 3. Combine and serve."
        )
    
    recipes = Recipe.objects.all()
    data = [
        {
            "name": recipe.name,
            "image_url": recipe.image_url,
            "instructions": recipe.instructions,
        }
        for recipe in recipes
    ]
    return JsonResponse(data, safe=False)
