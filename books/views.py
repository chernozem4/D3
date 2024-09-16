from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .models import Book
from .forms import BookForm


# Для отображения полной информации о книге
def book_detail_view(request, id):
    if request.method == 'GET':
        post_id = get_object_or_404(models.Post, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'post_id': post_id
            }
        )




# вывод не полной информации
def book_list_view(request):
    if request.method == "GET":
        # query запрос
        post_object = models.Post.objects.all()
        return render(
            request,
            template_name='book_list.html',
            context={
                'post_object': post_object
            }
        )



from .models import Cloth, Tag

def filter_products(request):
    tag_name = request.GET.get('tag')
    if tag_name:
        tag = Tag.objects.filter(name=tag_name).first()
        products = Cloth.objects.filter(tags=tag)
    else:
        products = Cloth.objects.all()

    tags = Tag.objects.all()
    return render(request, 'filter_products.html', {'products': products, 'tags': tags})






# Чтение всех книг (Read)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Просмотр одной книги
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

# Создание новой книги (Create)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

# Обновление книги (Update)
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

# Удаление книги (Delete)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})





















#def about_me(request):
#    return HttpResponse("Информация обо мне: Ваше имя, возраст, увлечения.")

#def about_friend(request):
#    return HttpResponse("Информация о друге: Имя друга, возраст, увлечения.")

#def current_time(request):
#    now = datetime.now()
#    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
#    return HttpResponse(f"Текущее время: {current_time}")

