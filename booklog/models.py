from django.db import models
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30, default=' ')
    review_type = models.TextChoices('ReviewType', 'Good Bad Terrible')
    image = models.ImageField(default='default.jpg', upload_to='book_profile')
    review = models.CharField(blank=False, choices=review_type.choices, max_length=10)
    
    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path) 
        
        if img.height > 400 or img.width > 320:
            output_size = (220, 333)
            img.thumbnail(output_size)
            img.save(self.image.path)
