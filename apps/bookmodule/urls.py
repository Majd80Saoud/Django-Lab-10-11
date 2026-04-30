from django.urls import path
from . import views



urlpatterns = [
   
    path('', views.index, name='index'),
    path('list/', views.list_books, name='list_books'),
   # path('about/', views.aboutus, name='aboutus'),

   # path('html5/lab5/', views.lab5, name='lab5'),

    #path('search/', views.search, name='search'),

   # path('simple/query', views.simple_query, name='simple_query'),

    # path('complex/query', views.complex_query, name='complex_query'),

    # path('lab8/task1', views.lab8_task1, name='lab8_task1'),

    # path('lab8/task2', views.lab8_task2, name='lab8_task2'),

    # path('lab8/task3', views.lab8_task3, name='lab8_task3'),

    # path('lab8/task4', views.lab8_task4, name='lab8_task4'),

    # path('lab8/task5', views.lab8_task5, name='lab8_task5'),

    # path('lab8/task7', views.lab8_task7, name='lab8_task7'),



    path('lab9/task1', views.lab9_task1),
    path('lab9/task2', views.lab9_task2),
    path('lab9/task3', views.lab9_task3),
    path('lab9/task4', views.lab9_task4),
    path('lab9/task5', views.lab9_task5),
    path('lab9/task6', views.lab9_task6),




    path('lab9_part1/listbooks', views.list_books_part1, name='list_books_part1'),
    path('lab9_part1/addbook', views.add_book_part1, name='add_book_part1'),
    path('lab9_part1/editbook/<int:id>', views.edit_book_part1, name='edit_book_part1'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book_part1, name='delete_book_part1'),


    path('lab9_part2/listbooks', views.list_books_part2, name='list_books_part2'),
    path('lab9_part2/addbook', views.add_book_part2, name='add_book_part2'),
    path('lab9_part2/editbook/<int:id>', views.edit_book_part2, name='edit_book_part2'),
    path('lab9_part2/deletebook/<int:id>', views.delete_book_part2, name='delete_book_part2'),


  path('forms2/task1/students', views.list_students, name='list_students'),
  path('forms2/task1/add', views.add_student, name='add_student'),
  path('forms2/task1/edit/<int:id>', views.edit_student, name='edit_student'),
  path('forms2/task1/delete/<int:id>', views.delete_student, name='delete_student'), 

  path('forms2/task2/students', views.list_students2, name='list_students2'),
  path('forms2/task2/add', views.add_student2, name='add_student2'),
  path('forms2/task2/edit/<int:id>', views.edit_student2, name='edit_student2'),
  path('forms2/task2/delete/<int:id>', views.delete_student2, name='delete_student2'),



 path('forms2/task3/clubs', views.list_clubs, name='list_clubs'),
 path('forms2/task3/add', views.add_club, name='add_club'),
 path('forms2/task3/edit/<int:id>', views.edit_club, name='edit_club'),
 path('forms2/task3/delete/<int:id>', views.delete_club, name='delete_club'),
]