from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=20)
    email = models.EmailField(verbose_name='Почта')
    message = models.TextField(verbose_name='Пожелания')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзыв"
