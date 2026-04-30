# from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import redirect

from django.db.models import Q, Count, Sum, Avg, Max, Min     # for lab8
#from .models import Book  , Student ,Address                                     # for lab8

from .models import Book, Publisher, Author  #lab 9
from django.db import connection


#def index(request):
    #return HttpResponse("Hello world")



# def index(request):
   # name = request.GET.get("name") or "world"
     # return HttpResponse("Hello " + name)  



# def index2(request , vall=0):
    # return HttpResponse("value = " + str(vall))

#def index(request):
    #name = request.GET.get("namr") or "world"
   # return render(request , "bookmodule/index.html" , {"name" : name})  


#def viewbook(request, bookId):
    #book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
   # book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}

   # targetBook = None
    #if book1['id'] == bookId:
       # targetBook = book1
    #if book2['id'] == bookId:
       # targetBook = book2

   # context = {'book': targetBook}
   # return render(request, 'bookmodule/show.html', context)





from django.shortcuts import render

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, "bookmodule/list_books.html")

def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")




def lab5(request):
    return render(request, 'bookmodule/lab5.html')




def search(request):

    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False

            if isTitle and string in item['title'].lower():
                contained = True

            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]



from .models import Book
def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookListLab7.html', {'books': mybooks})



def complex_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False
    ).filter(
        title__icontains='and'
    ).filter(
        edition__gte=2
    ).exclude(
        price__lte=100
    )[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookListLab7.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    

def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookListLab7.html', {'books': books})


def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookListLab7.html', {'books': books})


def lab8_task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) & (~Q(title__icontains='qu') | ~Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookListLab7.html', {'books': books})



def lab8_task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/bookListLab7.html', {'books': books})


def lab8_task5(request):
    stats = Book.objects.aggregate(
        count_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/bookStats.html', {'stats': stats})


#def lab8_task7(request):
   # data = Student.objects.values('address__city').annotate(total=Count('id'))
   # return render(request, 'bookmodule/studentCityCount.html', {'data': data})








def lab9_task1(request):
    total = Book.objects.aggregate(total=Sum('quantity'))['total'] or 0
    books = Book.objects.all()

    for b in books:
        if total > 0:
            b.percentage = round((b.quantity / total) * 100, 2)
        else:
            b.percentage = 0

    return render(request, 'bookmodule/lab9_task1.html', {'books': books})


def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})


def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_book=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})


def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})


def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        high_books=Count('book', filter=Q(book__rating__gte=4))
    )
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})


def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books=Count(
            'book',
            filter=Q(book__price__gt=50) & Q(book__quantity__lt=5) & Q(book__quantity__gte=1)
        )
    )
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})



#Lab 10

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def list_books_part1(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part1/listbooks.html', {'books': books})

def add_book_part1(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            price=request.POST.get('price'),
            edition=request.POST.get('edition')
        )
        return redirect('list_books_part1')

    return render(request, 'bookmodule/lab9_part1/addbook.html')

def edit_book_part1(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('list_books_part1')

    return render(request, 'bookmodule/lab9_part1/editbook.html', {'book': book})

def delete_book_part1(request, id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM bookmodule_book WHERE id = %s", [id])

    return redirect('list_books_part1')

from .forms import BookForm

def list_books_part2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part2/listbooks.html', {'books': books})

def add_book_part2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books_part2')
    else:
        form = BookForm()

    return render(request, 'bookmodule/lab9_part2/addbook.html', {'form': form})

def edit_book_part2(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books_part2')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookmodule/lab9_part2/editbook.html', {'form': form})

def delete_book_part2(request, id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM bookmodule_book WHERE id = %s", [id])

    return redirect('list_books_part2')




#Lab 11

from .models import Student
from .forms import StudentForm

def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/lab_forms2/task1/list_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()

    return render(request, 'bookmodule/lab_forms2/task1/student_form.html', {'form': form})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)

    return render(request, 'bookmodule/lab_forms2/task1/student_form.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('list_students')



from .models import Student2
from .forms import Student2Form

def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/lab_forms2/task2/list_students2.html', {'students': students})

def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form()

    return render(request, 'bookmodule/lab_forms2/task2/student2_form.html', {'form': form})

def edit_student2(request, id):
    student = get_object_or_404(Student2, id=id)

    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form(instance=student)

    return render(request, 'bookmodule/lab_forms2/task2/student2_form.html', {'form': form})

def delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    student.delete()
    return redirect('list_students2')


from .models import Club
from .forms import ClubForm

def list_clubs(request):
    clubs = Club.objects.all()
    return render(request, 'bookmodule/lab_forms2/task3/list_clubs.html', {'clubs': clubs})

def add_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_clubs')
    else:
        form = ClubForm()

    return render(request, 'bookmodule/lab_forms2/task3/club_form.html', {'form': form})

def edit_club(request, id):
    club = get_object_or_404(Club, id=id)

    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES, instance=club)
        if form.is_valid():
            form.save()
            return redirect('list_clubs')
    else:
        form = ClubForm(instance=club)

    return render(request, 'bookmodule/lab_forms2/task3/club_form.html', {'form': form})

def delete_club(request, id):
    club = get_object_or_404(Club, id=id)
    club.delete()
    return redirect('list_clubs')







