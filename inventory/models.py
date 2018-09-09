from django.db import models

class Order(models.Model):
        id = models.BigIntegerField(primary_key=True)
        email = models.EmailField(max_length=255)
        closed_at = models.DateTimeField('date closed')
        created_at = models.DateTimeField('date created')
        updated_at = models.DateTimeField('date updated')
        number = models.IntegerField()
        note = models.CharField(max_length=255)
        token = models.CharField(max_length=255)
        gateway = models.GenericIPAddressField(protocol='both')
        test = models.BooleanField()
        total_price = models.FloatField()
        subtotal_price = models.FloatField()
        total_weight = models.FloatField()
        total_tax = models.FloatField()

        def __str__(self):
            return self.id