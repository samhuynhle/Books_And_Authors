from django.shortcuts import render, redirect
from .models import *

def books_home(request):
    request.session['current_page'] = 'books_home'
    create_table_for_home(request, request.session['current_page'])

    return render(request,'books_authors_app/index.html')

    
def authors_home(request):
    request.session['current_page'] = 'authors_home'
    create_table_for_home(request, request.session['current_page'])

    return render(request,'books_authors_app/index2.html')

def display_books(request, id):
    this_book = Book.objects.filter(id=int(id))
    request.session['book_id'] = int(id)
    request.session['book_title'] = this_book[0].title
    request.session['book_description'] = this_book[0].description

    test_list = []
    print_list = []
    for a in this_book[0].authors.all():
        print_list.append(f"{a.first_name} {a.last_name}")
        test_list.append(a.first_name)
    request.session['book_authors'] = print_list

    request.session['all_authors'] = []

    request.session['for_print_authors'] = []
    for a in Author.objects.all():
        if a.first_name not in test_list:
            request.session['for_print_authors'].append(f"<option value='{a.id}'>{a.first_name} {a.last_name}</option>")

    return render(request,'books_authors_app/display.html')

def display_authors(request, id):
    this_author = Author.objects.filter(id=int(id))
    request.session['author_id'] = int(id)
    request.session['author_first_name'] = this_author[0].first_name
    request.session['author_last_name'] = this_author[0].last_name
    request.session['author_notes'] = this_author[0].notes

    print_list = []
    for a in this_author[0].books.all():
        print_list.append(f"{a.title}")
    request.session['author_books'] = print_list

    request.session['all_books'] = []

    request.session['for_print_books'] = []
    for a in Book.objects.all():
        if a.title not in print_list:
            request.session['for_print_books'].append(f"<option value='{a.id}'>{a.title}</option>")

    return render(request,'books_authors_app/display_author.html')

def add_them(request):
    if request.session['current_page'] == 'authors_home':
        if request.method == "POST":
            current_author = Author.objects.get(id=int(request.POST['author_id']))
            current_book = Book.objects.get(id=int(request.POST['book']))

            current_book.authors.add(current_author)
            current_book.save()
        return redirect('/authors')

    if request.session['current_page'] == 'books_home':
        if request.method == "POST":
            current_book = Book.objects.get(id=int(request.POST['book_id']))
            current_author = Author.objects.get(id=int(request.POST['author']))

            current_book.authors.add(current_author)
            current_book.save()
        return redirect('/')


def processing(request):
    if request.session['current_page'] == 'authors_home':
        if request.method == "POST":
            new_entry = Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])
            new_entry.save()
        return redirect('/authors')
    if request.session['current_page'] == 'books_home':
        if request.method == "POST":
            new_entry = Book.objects.create(title = request.POST['title'], description = request.POST['description'])
            new_entry.save()
        return redirect('/')

def create_table_for_home(request, location):
    request.session['for_print'] = []
    if request.session['current_page'] == 'books_home':
        books = Book.objects.all()
        for x in range(0,len(books),1):
            action_url = f"<a href='/books/{books[x].id}'>View</a>"
            request.session['for_print'].append(f"<tr><th scope='col'>{books[x].id}</th><th scope='col'>{books[x].title}</th><th scope='col'>{action_url}</th></tr>")
    if request.session['current_page'] == 'authors_home':
        authors = Author.objects.all()
        for x in range(0,len(authors),1):
            action_url = f"<a href='/authors/{authors[x].id}'>View</a>"
            request.session['for_print'].append(f"<tr><th scope='col'>{authors[x].id}</th><th scope='col'>{authors[x].first_name} {authors[x].last_name}</th><th scope='col'>{action_url}</th></tr>")

    return redirect('/')