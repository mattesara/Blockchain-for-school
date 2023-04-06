from django.conf import settings
from django.db import models
from django.utils import timezone
from api.utils import sendTransaction
import hashlib


class Degree(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_degree = models.TextField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    date_degree = models.DateField()
    vote = models.DecimalField(max_digits=4, decimal_places=2)
    hash = models.CharField(max_length=66, blank=True, null=True)
    txId = models.CharField(max_length=66, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    def writeOnChain(self):
        self.data = f"{self.title_degree}{self.first_name}{self.last_name}{self.date_of_birth}{self.date_degree}{self.vote}"
        self.hash = hashlib.sha256(self.data.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()

