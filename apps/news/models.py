from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news', verbose_name='Фото')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'