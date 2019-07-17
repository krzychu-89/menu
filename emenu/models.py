from django.db import models
from menu_test.models import TimestampModel

# Create your models here.


class Menu(TimestampModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.name, self.description)

    class Meta:
        db_table = 'emenu\".\"menu'


class Dish(TimestampModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField()
    preparation_time = models.DurationField(blank=True, null=True)
    is_vegetarian = models.BooleanField(default=False)
    menu_id = models.ForeignKey(Menu, db_column='menu_id',
                                on_delete=models.CASCADE,
                                related_name='dishes')
    image = models.ImageField(upload_to='dish_image', blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.description)

    class Meta:
        db_table = 'emenu\".\"dish'
        verbose_name_plural = "dishes"
