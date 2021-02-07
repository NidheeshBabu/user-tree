from django.db import models

# Create your models here.

class tbl_user(models.Model):
    userId = models.IntegerField()
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    title = models.CharField(max_length = 30)
    parentNodeId = models.IntegerField()
    currentPoints = models.FloatField()
    userImage = models.CharField(max_length = 300)


    class Meta:
        db_table = "tbl_user"

#To generate automatic ID's.
class tbl_idgen(models.Model):
    user = models.IntegerField()

    class Meta:
        db_table = "tbl_idgen"
#user value in tbl_idgen is initialized to 0.
