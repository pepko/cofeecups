from about_me.models import Information_about_me
from django.shortcuts import render_to_response

def home(request):
    user = Information_about_me.objects.get(id=1)
    return render_to_response("main.html", {"user":user})



