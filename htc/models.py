from django.db import models


class ReadingTypes(models.Model):
    id = models.AutoField(primary_key=True)
    reading_type = models.TextField(null=False)

    class Meta:
        managed = True
        db_table = 'reading_types'

    def __str__(self):
        return f"{self.reading_type}"

class Reading(models.Model):
    id = models.AutoField(primary_key=True)
    read_type = models.ForeignKey(ReadingTypes, on_delete=models.PROTECT)
    date_time = models.DateTimeField(blank=False, null=False,auto_now=True)
    value = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'reading'

    def __str__(self):
        return f"{self.id} - {self.read_type} - {self.value}  - {self.date_time}"
    