from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def staff(request):
    return render(request, 'staff.html')


def customer(request):
    return render(request, 'customer.html')


def activity(request):
    return render(request, 'activity.html')


def leave(request):
    return render(request, 'leave.html')
