from django.shortcuts import render
from .models import Meal, MealPlan, Recipe, Nutrition

# Create your views here.
def meal_list(request):
    meals = Meal.objects.all()
    return render(request, 'meals/meal_list.html', {'meals': meals})

def meal_detail(request, meal_id):
    meal = Meal.objects.get(pk=meal_id)
    return render(request, 'meals/meal_detail.html', {'meal': meal})
