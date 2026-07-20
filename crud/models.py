from timestamps.models import models, Model
from datetime import datetime

class Student(Model):
    class Meta :
        db_table='students'
        db_table_comment='test meta data for student model'
        
    name = models.CharField(max_length=50)
    born_date = models.DateField()
    nationality = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime.now())
class Subject(Model):
    class Meta:
        db_table = 'subjects'
    name = models.CharField()
    category = models.CharField() # math /info etc 
    created_at = models.DateTimeField(default=datetime.now())
