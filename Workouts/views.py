from django.shortcuts import render
from .models import Workout, Exercise, WorkoutExercise, WorkoutLog
from django.http import HttpResponse

# Create your views here.
def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

def workout_detail(request, workout_id):
    workout = Workout.objects.get(pk=workout_id)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})

#Luis testing:
def workout(request):
    return HttpResponse("Hello, welcome to the Workout Page") 


