from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Programme, Student, Item
from .forms import DepartmentForm, ProgrammeForm, StudentForm, ItemForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def dashboard(request):
    context = {
        'total_students': Student.objects.count(),
        'total_departments': Department.objects.count(),
        'total_programmes': Programme.objects.count(),
        'total_items': Item.objects.count(),
    }
    username = request.session.get('username')
    return render(request, "sports_attendance/dashboard.html", {"username": username})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = user.username  # Store username in session
            
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "sports_attendance/login.html")


def user_logout(request):
    logout(request)
    request.session.flush()  # Clear session data
    return redirect("login")  # Redirect to login page after logout


# Manage Departments
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'sports_attendance/department_list.html', {'departments': departments})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'sports_attendance/department_form.html', {'form': form})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'sports_attendance/department_form.html', {'form': form})



# Manage Programmes
def programme_list(request):
    programmes = Programme.objects.all()
    return render(request, 'sports_attendance/programme_list.html', {'programmes': programmes})

def programme_create(request):
    if request.method == 'POST':
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programme_list')
    else:
        form = ProgrammeForm()
    return render(request, 'sports_attendance/programme_form.html', {'form': form})

def programme_update(request, pk):
    programme = get_object_or_404(Programme, pk=pk)
    if request.method == 'POST':
        form = ProgrammeForm(request.POST, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('programme_list')
    else:
        form = ProgrammeForm(instance=programme)
    return render(request, 'sports_attendance/programme_form.html', {'form': form})



# Manage Students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'sports_attendance/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'sports_attendance/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'sports_attendance/student_form.html', {'form': form})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'sports_attendance/item_list.html', {'items': items})

# Create a new item
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'sports_attendance/item_form.html', {'form': form, 'title': 'Add Item'})

# Update an existing item
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'sports_attendance/item_form.html', {'form': form, 'title': 'Edit Item'})

# Delete an item
#def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'items/item_confirm_delete.html', {'item': item})
