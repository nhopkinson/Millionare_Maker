from django.db import models


class Member(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name