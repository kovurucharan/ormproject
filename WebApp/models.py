from django.db import models

class State(models.Model):
    Sname=models.CharField(max_length=100)
    def __str__(self):
        return self.Sname


class Capitalcity(models.Model):
    Cname=models.CharField(max_length=100)
    State=models.OneToOneField(State,on_delete=models.CASCADE)
    def __str__(self):
        return self.Cname
