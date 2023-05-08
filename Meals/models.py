from django.db import models
from django.contrib.auth.models import User

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

class Meal(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    calories = models.IntegerField()
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)

class Nutrition(models.Model):
    meal = models.OneToOneField(Meal, on_delete=models.CASCADE)
    protein = models.FloatField()  # Protein in grams
    carbohydrates = models.FloatField()  # Carbohydrates in grams
    fats = models.FloatField()  # Fats in grams
    fiber = models.FloatField()  # Fiber in grams

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField()  # Preparation time in minutes
    cook_time = models.IntegerField()  # Cooking time in minutes
