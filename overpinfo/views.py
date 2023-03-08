from django.shortcuts import render


def overp_info(request):
    
    context = {}
    return render(request, 'overpinfo/overpinfo.html', context)