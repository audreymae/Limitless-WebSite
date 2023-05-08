from django.shortcuts import render
from .models import Workout, Exercise, WorkoutExercise, WorkoutLog

# Create your views here.
def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

def workout_detail(request, workout_id):
    workout = Workout.objects.get(pk=workout_id)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})
