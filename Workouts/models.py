from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    muscle_group = models.CharField(max_length=100)  # e.g., 'chest', 'legs', 'arms'
    equipment_required = models.CharField(max_length=100, blank=True, null=True)  # e.g., 'dumbbell', 'barbell', 'bodyweight'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # Duration in minutes
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest_time = models.IntegerField()  # Rest time in seconds

class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date_completed = models.DateField()
    duration = models.IntegerField()  # Duration in minutes
