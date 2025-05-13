from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Faculty
from .forms import FacultyForm

def home(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty/home.html', {'faculties': faculties})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'faculty/login.html', {'form': form})

@login_required
def dashboard(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty/dashboard.html', {'faculties': faculties})

@login_required
def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FacultyForm()
    return render(request, 'faculty/add_faculty.html', {'form': form})

@login_required
def edit_faculty(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        form = FacultyForm(request.POST, request.FILES, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FacultyForm(instance=faculty)
    return render(request, 'faculty/edit_faculty.html', {'form': form, 'faculty': faculty})

@login_required
def delete_faculty(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        faculty.delete()
        return redirect('dashboard')
    return render(request, 'faculty/delete_faculty.html', {'faculty': faculty})