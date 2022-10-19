# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, UserRegistrationForm, TeacherRegistrationForm
from apps.stafff.models import Profile


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("profile")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            # Set the chosen password:using teh set_password() allows encryption
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()

            # Create the user profile
            Profile.objects.create(user=new_user)
    
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            print('username: ', username)

            msg = f'Hello {user}! Your account has been created - please <a href="/login">login</a> to continue.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = UserRegistrationForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def register_teacher(request):
    msg = None
    success = False

    if request.method == "POST":
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            # Set the chosen password:using teh set_password() allows encryption
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()

            # Create the user profile
            Profile.objects.create(user=new_user)
    
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            print('username: ', username)

            msg = f'Hello {user}! Your account has been created - please <a href="/login">login</a> to continue.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = TeacherRegistrationForm()

    return render(request, "accounts/registers.html", {"form": form, "msg": msg, "success": success})