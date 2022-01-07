from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField('Название', max_length=30)
    short_text = models.CharField('Краткое опимание', max_length=50)
    full_text = models.TextField('Текст')
    image = models.ImageField(verbose_name='Картинка', upload_to='static/media', height_field=None, width_field=None, max_length=100)
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


