from django.shortcuts import render


def Tracker(request):
    
    context = {}
    return render(request, 'Tracker/tracker.html', context)