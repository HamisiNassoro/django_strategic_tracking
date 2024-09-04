from django.shortcuts import render, redirect
from .models import StrategicObjective, KeyActivity
from .forms import StrategicObjectiveForm, KeyActivityForm

# View to create a new Strategic Objective
def create_objective(request):
    if request.method == 'POST':
        form = StrategicObjectiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objective_list')
    else:
        form = StrategicObjectiveForm()
    return render(request, 'strategy/create_objective.html', {'form': form})

# View to list all Strategic Objectives
def objective_list(request):
    objectives = StrategicObjective.objects.all()
    return render(request, 'strategy/objective_list.html', {'objectives': objectives})

# View to create a new Key Activity
def create_activity(request):
    if request.method == 'POST':
        form = KeyActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = KeyActivityForm()
    return render(request, 'strategy/create_activity.html', {'form': form})

# View to list all Key Activities
def activity_list(request):
    activities = KeyActivity.objects.all()
    return render(request, 'strategy/activity_list.html', {'activities': activities})
