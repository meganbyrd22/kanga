from django.http import JsonResponse
from .models import Recipe

def recipe_list(request):
    
    # Create hardcoded recipes if none exist
    if Recipe.objects.count() == 0:
        print("Creating hardcoded recipes...")  # Debug output
        Recipe.objects.create(
            name="Tortellini Pasta Salad",
            image_url="https://lemonsandzest.com/wp-content/uploads/2021/04/Tortellini-Caprese-Pasta-Salad-2.10.jpg",
            instructions="<a href='https://lemonsandzest.com/tortellini-caprese-salad/'>Click here for recipe instructions</a>",
            description="A delicious tortellini pasta salad with fresh ingredients."
        )
        Recipe.objects.create(
            name="Pickle Cheeseburger Bites",
            image_url="https://hips.hearstapps.com/hmg-prod/images/dill-pickle-cheeseburger-bites-665a2063ad61a.jpg?crop=0.713xw:0.476xh;0.262xw,0.406xh&resize=1200:*",
            instructions="<a href='https://www.thepioneerwoman.com/food-cooking/recipes/a60964027/pickle-cheeseburger-bites-recipe/'>Click here for recipe instructions</a>",
            description="Mini cheeseburgers with a pickle twist."
        )
        Recipe.objects.create(
            name="Ranch Slaw",
            image_url="https://hips.hearstapps.com/hmg-prod/images/ranch-slaw-recipe-664368bf4bfb3.jpg?crop=0.884xw:0.884xh;0.112xw,0.0425xh&resize=1200:*",
            instructions="<a href='https://www.thepioneerwoman.com/food-cooking/recipes/a60787797/ranch-slaw-recipe/'>Click here for recipe instructions</a>",
            description="A crunchy and creamy slaw with a ranch dressing."
        )
    
    # Retrieve all recipes from the database
    recipes = Recipe.objects.all()
    
    # Prepare the data to be returned as JSON
    data = [
        {
            "name": recipe.name,
            "image_url": recipe.image_url,
            "instructions": recipe.instructions,
            "description": recipe.description,
        }
        for recipe in recipes
    ]
    print("Returning JSON response:", data)  # Debug output
    
    # Return the JSON response
    return JsonResponse(data, safe=False)
