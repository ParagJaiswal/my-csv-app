from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
import csv

# Create your views here.

def index(request):
    stu = Student.objects.all().order_by('first_name')
    return render(request,'app1/index.html',{'students':stu})


def get_csv_file(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="file.csv"'
    students = Student.objects.all().order_by('first_name')
    writer = csv.writer(response)
    writer.writerow(["First Name", "Last Name", "Address", "Mobile"])
    writer.writerow([])
    for student in students:
        writer.writerow([student.first_name, student.last_name, student.address, student.mobile])

    return response
