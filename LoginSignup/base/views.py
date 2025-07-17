from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Home page: show form + all students
def student_form_view(request):
    students = Student.objects.all()
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_form')

    return render(request, 'registration/student_form.html', {
        'form': form,
        'students': students
    })

# Delete view
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_form')

# Edit view
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_form')
    else:
        form = StudentForm(instance=student)

    return render(request, 'registration/edit_student.html', {
        'form': form
    })
