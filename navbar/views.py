from django.shortcuts import render
y

def overp_info(request):
    
    context = {'company': company}
    return render(request, 'overpinfo/overpinfo.html', context)