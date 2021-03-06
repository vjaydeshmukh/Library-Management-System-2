from django.conf import settings
from django.db import models
from django.db.models import Sum

from users.models import Member


class Bill(models.Model):
    title = models.CharField(max_length=settings.CHARFIELD_MAX_LENGTH)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} containing {self.billitem_set.count()} items'


class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    title = models.CharField(max_length=settings.CHARFIELD_MAX_LENGTH)
    description = models.TextField(max_length=settings.TEXTFIELD_MAX_LENGTH)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.price} - {self.title} for {self.bill}'


class Payment(models.Model):
    CASH = 10
    CREDIT = 20
    CARD_TO_CARD = 30
    BALANCE = 40
    PAYMENT_CHOICES = (
        (CASH, 'Cash'),
        (CREDIT, 'Credit Card'),
        (CARD_TO_CARD, 'Card to Card'),
        (BALANCE, 'Balance'),
    )
    reference_num = models.CharField(max_length=20, null=True, blank=True)
    payment_type = models.IntegerField(choices=PAYMENT_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    successful = models.BooleanField(default=False)

    @property
    def get_total(self):
        return self.bill.billitem_set.all().aggregate(Sum('price'))['price__sum']

    def __str__(self):
        return f'{self.get_total} Rial on {self.timestamp}'
