from django.contrib.auth.models import User
from django.db import models


class Livre(models.Model):
    objects = None
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    description = models.TextField()
    date_publication = models.DateField()
    image = models.ImageField(upload_to='livres_images', null=True, blank=True)

    def __str__(self):
        return self.titre


class Emprunt(models.Model):
    objects = None
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.utilisateur.username} emprunte {self.livre.titre}"
