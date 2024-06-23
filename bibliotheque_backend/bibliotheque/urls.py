from django.urls import path
from . import views

app_name = 'bibliotheque'

urlpatterns = [
    path('', views.liste_livres, name='liste_livres'),
    path('livres_emprunts/', views.livres_emprunts, name='livres_emprunts'),
    path('<int:livre_id>/', views.details_livre, name='details_livre'),
    path('<int:livre_id>/emprunter/', views.emprunter_livre, name='emprunter_livre'),
]