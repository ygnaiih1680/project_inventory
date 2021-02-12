from django.db import models


class Book(models.Model):
    class Meta:
        db_table = "book"

    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.TextField()
    contents = models.TextField()
    authors = models.TextField()
