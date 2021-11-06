from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class todo(models.Model):
    status_choice = [
        ('C', 'complete'),
        ('P', 'pending')
    ]
    priority_choice = [
        ('1', '1️⃣️'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),
        ('6', '6️⃣'),
        ('7', '7️⃣'),
        ('8', '8️⃣'),
        ('9', '9️⃣'),
        ('10', '🔟')

    ]
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=status_choice)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2, choices=priority_choice)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
