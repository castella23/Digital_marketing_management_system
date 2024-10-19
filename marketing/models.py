from django.db import models

# Create your models here.
class Campany(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Campany_name'

    # company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
    # name = models.CharField(max_length=100)
    # description = models.TextField(blank=True, null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # created_at = models.DateTimeField(auto_now_add=True)