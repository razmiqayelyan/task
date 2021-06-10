from django.db import models
import random 

'''     "citizens": [{
        "citizen_id": 1,
        "town": "Yerevan",
        "street": "Sayat Nova",
        "building": "16",
        "appartement": 7,
        "name": "Poghosyan Poghos",
        "birth_date": "01.02.2000",
        "gender": "male",
        "relatives": [2, 28]
	},] } '''
pol = (
	('male', 'male'),
	('female', 'female')
	)

x = random.randint(0, 999)
# Create your models here.
class Giftshop(models.Model):
	citizen_id = models.IntegerField(default=x, null=False, blank=False)
	town = models.CharField(max_length=100, null=False, blank=False)
	street = models.CharField(max_length=100, null=False, blank=False)
	building = models.CharField(max_length=100, null=False, blank=False)
	appartement = models.CharField(max_length=100, null=False, blank=False)
	name = models.CharField(max_length=100, null=False, blank=False)
	birth_date = models.CharField(max_length=20, null=False, blank=False)
	gender = models.CharField(max_length=7, null=False, blank=False)
	relatives = models.CharField(max_length=100, null=False, blank=False)

	def __str__(self):
		return f'ID:{self.citizen_id} | Name:{self.name}'



# class Birthdays(models.Model):
# 	data = models.ForeignKey(Giftshop, on_delete=models.CASCADE)
# 	month = models.CharField(max_length=2, default=citizen_id[4:6])