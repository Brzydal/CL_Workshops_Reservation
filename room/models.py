from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    projector = models.BooleanField()
    
    def __str__(self):
        return '{}-{}/{}'.format(self.name,self.capacity,self.projector)
    
class Reservation(models.Model):
    date = models.DateField()
    comment = models.TextField()
    room_id = models.ForeignKey(Room)
    
    def __str__(self):
        return '{}/{}'.format(self.date,self.comment)
