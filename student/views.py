from django.shortcuts import render

# Create your views here.


def student_dashboard(request):
    return render(request, "student_dashboard.html", {})

def professor_dashboard(request):
    return render(request, "professor_dashboard.html", {})