import json
import os
import time
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BENUTZER_DATEI = os.path.join(BASE_DIR, "benutzer.json")



def login(request):
    with open(BENUTZER_DATEI, "r") as f:
        users = json.load(f)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        for u in users:
            if u["username"] == username and u["password"] == password:
                request.session["username"] = username
                return redirect("dashboard")

    return render(request, "meine_app/login.html")


def register(request):
    with open(BENUTZER_DATEI, "r") as f:
        users = json.load(f)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        users.append(
            {
                "username": username,
                "password": password,
            }
        )

        with open(BENUTZER_DATEI, "w") as f:
            json.dump(users, f, indent=2)

        return redirect("login")

    return render(request, "meine_app/register.html")


def logout(request):
    request.session.flush()
    return redirect("login")