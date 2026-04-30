import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryproject.settings')
django.setup()

from apps.bookmodule.models import Publisher, Author, Book

Publisher.objects.all().delete()
Author.objects.all().delete()
Book.objects.all().delete()

publishers = {}
authors = {}

with open('publishers.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        p = Publisher.objects.create(
            name=row['name'],
            location=row['location']
        )
        publishers[int(row['id'])] = p

with open('authors.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        a = Author.objects.create(
            name=row['name'],
            DOB=row['DOB']
        )
        authors[int(row['id'])] = a

with open('books.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        book = Book.objects.create(
            title=row['title'],
            price=float(row['price']),
            quantity=int(row['quantity']),
            pubdate=row['pubdate'],
            rating=int(row['rating']),
            publisher=publishers[int(row['publisher_id'])]
        )

        ids = row['author_ids'].split('|')
        for aid in ids:
            book.authors.add(authors[int(aid)])

print("Data loaded successfully!")