from django.db import models

class Serie(models.Model):
    serie_id = models.AutoField(primary_key=True)
    serie_text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.serie_text)

class Datum(models.Model):
    datum_id = models.AutoField(primary_key=True)
    datum_value = models.BigIntegerField()
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

    class Meta:
         verbose_name = 'datum'
         verbose_name_plural = 'data'