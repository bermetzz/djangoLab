from django.db import models


class Book(models.Model):
    GENRE = (
        ('Science Fiction', 'Science Fiction'),
        ('Horror', 'Horror'),
        ('Classics', 'Classics'),
        ('Detective and Mystery', 'Detective and Mystery'),
        ('Romance', 'Romance'),
        ('Biographies and Autobiographies', 'Biographies and Autobiographies'),
    )

    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    cost = models.CharField(max_length=30)
    genre = models.CharField(max_length=100, choices=GENRE, default=GENRE[2], null=True)
    url = models.URLField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
