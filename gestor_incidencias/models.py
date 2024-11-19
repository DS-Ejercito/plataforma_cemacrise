from django.db import models

# Create your models here.
class procedencia(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()    
    descrip_larga = models.TextField()    
    cod_proced_superior = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategorias')
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila
    
class tp_incidencia(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    nom_img =  models.TextField(null=True)
    def __str__(self):
        fila =  str(self.descrip_corta)
        return fila
    
class depto(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila

class munic(models.Model):
    id = models.AutoField(primary_key=True)
    descrip_corta = models.TextField()
    cod_depto = models.ForeignKey(depto, on_delete=models.CASCADE, null=True, blank=True, related_name='subcategorias')
    def __str__(self):
        fila = str(self.descrip_corta)
        return fila

class incidencia(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    procedencia = models.ForeignKey(procedencia, on_delete=models.CASCADE)
    tp_incidencia = models.ForeignKey(tp_incidencia, on_delete=models.CASCADE)
    depto = models.ForeignKey(depto, on_delete=models.CASCADE)
    munic = models.ForeignKey(munic, on_delete=models.CASCADE)
    obser = models.TextField(blank=True, null=True)
    longitud = models.FloatField(null = True)
    latitud = models.FloatField(null = True)
    cant = models.FloatField(null = True)
    img = models.FileField(upload_to='Incidencias/', null = True, blank= True)
    def __str__(self):
        fila = "- Descripcion:" + str(self.fecha)
        return fila
    