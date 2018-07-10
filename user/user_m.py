from django.db import models

class User(models.Model):
    # primary_key 반드시 선언
    user_id = models.BigIntegerField(primary_key= True, max_length=11)
    email = models.CharField(max_length=100)
    login_platform = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


    class Meta:
        managed = False
        db_table = 'User'
