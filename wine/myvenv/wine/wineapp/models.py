from django.db import models

# Create your models here.
class Candidate(models.Model): # class이름은 대문자로 시작
    name = models.CharField(max_Lenth=10)
    introduction = models.TextField()
    area = models.CharField(max_Length=15)
    party_number = models.IntegerField(default=1)