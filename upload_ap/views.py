from django.shortcuts import render

# Create your views here.

def upload(request):
    context = {}
    return render(
        request,   # zapros
        'upload_ap/table.html',  # put k shablonu
                                # podstanovka
        context
    )