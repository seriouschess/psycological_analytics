from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def login(request):
    try:
        del request.session["user_id"] #you're a suspicious operation
    except:
        pass
    if request.method == "POST":
        if len(User.objects.filter(username = request.POST["username"])) == 0: #register
            subject = User.objects.create(username=request.POST["username"], password=request.POST["password"], surveyed=False)
            request.session["user_id"] = subject.id
            return redirect("/survey")
        else:
            if request.POST["password"] != User.objects.filter(username = request.POST["username"]).first().password: #fail
                messages.error(request, "Non matching password for existing user.")
                return redirect("/")
            else: #login
                request.session["user_id"] = User.objects.filter(username = request.POST["username"]).first().id
                return redirect("/survey")
    context={
        "users":User.objects.all()
    }
    return render(request, "login_app/index.html", context)
