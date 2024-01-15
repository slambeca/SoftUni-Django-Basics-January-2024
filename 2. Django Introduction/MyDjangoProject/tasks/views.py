from django import http

from django.shortcuts import render

from MyDjangoProject.tasks.models import Task

# Create your views here.
'''
Function based views
1. A function that has one or more params
2. Returns a response
'''


# def index(request):
#     name = request.GET.get("name", "NONAME")
#     content = "<h1>It works!</h1>" + \
#         f"<p>Welcome to the real world, {name}.</p>"
#     return http.HttpResponse(content,
#                              # headers={
#                              #     "Content-Type": "application/json",
#                              # }
#                              )

# def index(request):
#     title_filter = request.GET.get("filter", None)
#
#     tasks = Task.objects.all()
#
#     if title_filter:
#         tasks = tasks.filter(title__icontains=title_filter.lower())
#
#     if not tasks:
#         return http.HttpResponse("<h1>There are no tasks!</h1>")
#
#     result = []
#
#     for task in tasks:
#         result.append(f"""
#         <li>
#             <h2>{task.title}</h2>
#             <p>{task.description}</p>
#         </li>
#
#         """)
#
#     ul = f"<ul>{''.join(result)}</ul>"
#
#     content = f"""
#     <h1>{len(tasks)} Tasks</h1>
#     {ul}
#     """
#
#     return http.HttpResponse(content)

def index(request):
    title_filter = request.GET.get("filter", None)
    tasks = Task.objects.all()

    if title_filter:
        tasks = tasks.filter(title__icontains=title_filter.lower())

    context = {
        "title": "My Simple To-Do App",
        "tasks": tasks,
        "tasks_count": tasks.count(),
        "tasks_completed": tasks.filter(is_completed=True),
        "tasks_uncompleted": tasks.filter(is_completed=False),
    }

    return render(request,
                  "tasks/index.html",
                  context,
                  )