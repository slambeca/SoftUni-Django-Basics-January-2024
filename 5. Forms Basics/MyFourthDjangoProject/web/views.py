from django.shortcuts import render, redirect

from MyFourthDjangoProject.web.forms import EmployeeForm


def index(request):
    if request.method == "GET":
        context = {
            "employee_form": EmployeeForm(),
        }

        return render(request, "web/index.html", context)

    else:    # If request.method == "POST"
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # data is valid, populate "cleaned_data"
            # use the data in some way
            # redirect to some URL
            return redirect("index")
        else:
            context = {
                "employee_form": form,
            }

            return render(request, "web/index.html", context)


# def index(request):
#     if request.method == "POST":
#         form = EmployeeForm(request.POST or None)
#     else:
#         form = EmployeeForm()

#     if request.method == "POST":
#        if form.is_valid():
#            return redirect("index")
#
#     context = {"employee_form": form}
#
#     return render(request, "web/index.html", context)