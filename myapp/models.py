from django.db import models
from django import forms


class Departement(models.Model):
    num = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=40)
    numChef = models.IntegerField()
    numAgendaDept = models.ForeignKey('AgendaDept', on_delete=models.CASCADE)

    def __str__(self):

        
        return self.nom

class Agenda(models.Model):
    numAgenda = models.IntegerField(primary_key=True)
    dateCreation = models.DateField()
    numEmploye = models.ForeignKey('Employe', on_delete=models.CASCADE,default=0)

    def __str__(self):
        return str(self.numAgenda)


class AgendaDept(models.Model):
    numAgendaDept = models.IntegerField(primary_key=True)
    dateMAJ = models.DateField()

    def __str__(self):
        return str(self.numAgendaDept)

class Employe(models.Model):
    numEmploye = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=20)
    telIntern = models.CharField(max_length=14)
    email = models.CharField(max_length=40)
    niveau = models.IntegerField()
    numDept = models.ForeignKey('Departement', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
class ProcesVerbal(models.Model):
    NumProcesV = models.IntegerField(primary_key=True)
    resum = models.CharField(max_length=1024)

    def __str__(self):
        return f"ProcesVerbal: {self.NumProcesV}"

class ActivitesDept(models.Model):
    numAct = models.IntegerField(primary_key=True)
    typeD = models.CharField(max_length=20)
    descript = models.CharField(max_length=1024)
    dateAct = models.DateField()
    hDebut = models.TimeField(blank=True, null=True)
    hFin = models.TimeField(blank=True, null=True)
    dateCreation = models.DateField()
    createur = models.CharField(max_length=20)
    numAgenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)

    def __str__(self):
        return f"ActivitesDept: {self.numAct}"

class ActDeptVerbal(models.Model):
    numAct = models.ForeignKey(ActivitesDept, on_delete=models.CASCADE)
    numProcesV = models.ForeignKey(ProcesVerbal, on_delete=models.CASCADE)

    def __str__(self):
        return f"ActDeptVerbal: {self.numAct} - {self.numProcesV}"

class Absent(models.Model):
    numEmploye = models.ForeignKey(Employe, on_delete=models.CASCADE)
    numActDept = models.ForeignKey(ActivitesDept, on_delete=models.CASCADE)
    motif = models.CharField(max_length=1024)

    def __str__(self):
        return f"Absent: {self.numEmploye} - {self.numActDept}"

class Activites(models.Model):
    numActivite = models.IntegerField(primary_key=True)
    typeA = models.CharField(max_length=30)
    description = models.CharField(max_length=1024)
    dateAct = models.DateField()
    hDebut = models.TimeField(blank=True, null=True)
    hFin = models.TimeField(blank=True, null=True)
    dateCreation = models.DateField()
    createur = models.CharField(max_length=20)
    visible = models.IntegerField()
    numAgenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)

    def __str__(self):
        return f"Activites: {self.numActivite}"

class Alertes(models.Model):
    type = models.CharField(max_length=8)
    delais = models.DateField()
    numActivite = models.ForeignKey(Activites, on_delete=models.CASCADE)

    def __str__(self):
        return f"Alertes: {self.type} - {self.delais}"
