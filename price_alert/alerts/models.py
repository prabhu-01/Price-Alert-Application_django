from django.db import models
from django.conf import settings

class Alert(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('triggered', 'Triggered'),
        ('deleted', 'Deleted'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cryptocurrency = models.CharField(max_length=50)
    target_price = models.DecimalField(max_digits=15, decimal_places=2)
    current_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cryptocurrency} alert for {self.user.username} at ${self.target_price}'
