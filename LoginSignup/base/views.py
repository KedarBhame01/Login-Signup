from django.utils.encoding import smart_str

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.http import HttpResponse
#for export excel -
import openpyxl
# for export pdf -
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

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

def export_students_excel(request):
    students = Student.objects.all()
    
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Student'

    sheet.append(['ID','Name','Age'])
    
    for student in students:
        sheet.append([student.id, student.name, student.age])
        
    response = HttpResponse(
        content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=students_info.xlsx'
    
    workbook.save(response)
    return response

def export_students_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=students_info.pdf'

    p = canvas.Canvas(response,pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height -50, "Student List")

    p.setFont("Helvetica-Bold",12)
    p.drawString(50, height - 100, "ID")
    p.drawString(100, height -100, "Name")
    p.drawString(300, height - 100, "Age")

    y = height - 120
    p.setFont("Helvetica",12)
    
    students = Student.objects.all()
    for student in students:
        p.drawString(50, y, str(student.id))
        p.drawString(100, y, student.name)
        p.drawString(300, y, str(student.age))
        y -= 20
        if y < 50:
            p.showPage()
            y = height - 50
            
    p.showPage()
    p.save()
    return response