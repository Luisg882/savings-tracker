from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):   
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    slug = models.SlugField(max_length=200, unique=True)
    age = models.IntegerField()
    email = models.EmailField(max_length=200, unique=True)
    nominated_bank_account = models.CharField(max_length=100)
    main_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"this is {self.user}"

class SavingPot(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="saving_pots"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user"
    )
    name = models.CharField(max_length=200, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"this is {self.name}"

