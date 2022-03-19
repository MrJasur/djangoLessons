from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE   # bu degani, agar biz shu muallifni o'chirib yuborsak bu muallif yaratgan matnlar ham o'chib ketadi
    )
    body = models.TextField()

    def __str__(self):
        return self.title