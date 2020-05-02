from django.db import models

# Create your models here.
class Users(model.Models)
    name = models.CharFeild(max_lenghth=32)
    age = models.IntegerFeild()

    class Meta:
        db_table = 'user'
