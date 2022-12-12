from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

""" CARRERA = (
  ('Ing de Sistemas', 'Ing de Sistemas'),
  ('Ing Electrica', 'Ing Electrica'),
  ('Ing Electronica', 'Ing Electronica'),
  ('Ing Mecatronica', 'Ing Mecatronica'),
  ('Ing Industrial', 'Ing Industrial'),
  ('Ing Civil', 'Ing Civil'),
  ('Ing Quimica', 'Ing Quimica'),
  ('Ing de Alimentos', 'Ing de Alimentos'),
  ('Ing Ambiental', 'Ing Ambiental'),
  ('Ing en Telecomunicaciones', 'Ing en Telecomunicaciones'),
  ('Ing Mecanica', 'Ing Mecanica'),
  ('Arquitectura', 'Arquitectura'),
  ('Diseño Industrial', 'Diseño Industrial')
) """

# Create your models here.
class Task(models.Model):
  name = models.CharField(max_length=40)
  lastname = models.CharField(max_length=40)
  codigo = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
  email = models.EmailField(max_length=60)
  carrera = models.CharField(max_length=40)
  created = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  #important = models.BooleanField(default=False)

  def __str__(self):
    return self.name