from django.db import models


class Document(models.Model):
    dateRecord = models.TextField()
    lineusrid = models.TextField()
    clientid = models.TextField( default= '-1')
    clientnum = models.TextField( default= '-1' )
    takeMedecine = models.IntegerField( default=0 )
    changeMedecine = models.IntegerField( default=0 )
    docfile = models.FileField()


    class Meta:
        db_table = 'Document'