from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import  Project, Skill
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
# Create your views here.

def index(request):  
     projects = Project.objects.all()
     skills = Skill.objects.all()
     context = {"projects": projects, "skills": skills}

     return render(request, "huseyinweb/index.html", context)

def contact(request):
     if request.method == "POST":
          form = ContactForm(request.POST)
          if form.is_valid():
               name = form.cleaned_data["name"]
               email = form.cleaned_data["email"]
               message = form.cleaned_data["message"]
               form.save()
               messages.success(request, "Mesajın başarı ile alındı.")
               return render(request, "huseyinweb/contact.html", {"form": form})
     else:
          form = ContactForm()
     return render(request, "huseyinweb/contact.html", {"form": form})


               