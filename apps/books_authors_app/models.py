from django.db import models

# Create your models here. We are defining the classes here. THese are the equivalents for the tables in MySQL Work Bench.
# We do (models.Model) as a way to inherit from an existing Model class and get all the functionalities.

# After we are done creating our classes and updating our models.py, go back to the terminal and run makemigrations and migrate.
# After this, the talbe is now exists.

class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return f"<Book object: {self.title} ({self.id})>"

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.CharField(max_length=255)
    books = models.ManyToManyField(Book,related_name="authors")

    def __repr__(self):
        return f"<Author object: {self.first_name} ({self.id})>"