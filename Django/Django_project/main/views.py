from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def multiplication_table(request):
    return render(request, 'multiplicationTable.html')

def deyProgrammer(request):
    return render(request, 'deyProgrammer.html')
