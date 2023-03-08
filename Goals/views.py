from django.shortcuts import render


def Goals(request):
    
    context = {}
    return render(request, 'Goals/goals.html', context)