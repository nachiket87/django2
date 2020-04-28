from django.db import models
from django.utils import timezone
from PIL import Image

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30, default=' ')
    review_type = models.TextChoices('ReviewType', 'Good Bad Terrible')
    image = models.ImageField(default='default.jpg', upload_to='book_profile')
    review = models.CharField(blank=True, choices=review_type.choices, max_length=10)
    
    

    def __str__(self):
        return self.title
