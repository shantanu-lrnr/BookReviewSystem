from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.


class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction','Fiction'),
        ('non-fiction','Non-Fiction'),
        ('science','Science'),
        ('technology','Technology'),
        ('history','History'),
        ('other','Other'),

    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    author_info = models.URLField(max_length=200, unique=True,blank=True,null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField()
    genre = models.CharField(max_length=20,choices=GENRE_CHOICES)
    isbn = models.CharField('ISBN',max_length=13,unique=True)
    publication_date = models.DateField()
    average_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0),MaxValueValidator(5)],
        default = 0,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"pk": self.pk})
    

