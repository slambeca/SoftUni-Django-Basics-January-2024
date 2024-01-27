from django.shortcuts import render, redirect


def signup_user(request):
    context = {}

    return render(request, "accounts/register-page.html", context)


def signin_user(request):
    context = {}

    return render(request, "accounts/login-page.html", context)


def signout_user(request):
    return redirect("index")


def details_profile(request, pk):
    context = {}

    return render(request, "accounts/details_profile.html", context)


def edit_profile(request, pk):
    context = {}

    return render(request, "accounts/edit_profile.html", context)


def delete_profile(request, pk):
    context = {}

    return render(request, "accounts/delete_profile.html", context)