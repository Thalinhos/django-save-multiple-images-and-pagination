from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Todo, TodoImage
from .forms import TodoForm

def todo_list(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save()

            for image in request.FILES.getlist('images'):
                TodoImage.objects.create(todo=todo, image=image)

            return redirect('todo_list')
    else:
        form = TodoForm()

    todos = Todo.objects.order_by('-created_at')

    paginator = Paginator(todos, 5)  # 👈 5 todos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todos/todo_list.html', {
        'form': form,
        'page_obj': page_obj
    })
