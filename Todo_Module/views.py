from django.shortcuts import render

from Todo_Module.models import Todo


# Create your views here.


def Index(request):
    context = {
        'todos': Todo.objects.order_by('-priority').all()
    }
    return render(request, 'Todo_Module/Index.html', context)