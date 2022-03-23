from django.db import models



# Create your models here.
class Post(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    xabar = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.ism