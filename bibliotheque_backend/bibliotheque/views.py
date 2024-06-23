from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Livre, Emprunt


def liste_livres(request):
    livres = Livre.objects.all()
    emprunts_livres = Emprunt.objects.all()
    return render(request, 'bibliotheque/liste_livres.html', {'livres': livres, 'emprunts_livres': emprunts_livres})


def livres_emprunts(request):
    emprunts_des_livres = Emprunt.objects.all()
    return render(request, 'bibliotheque/livres_emprunts.html', {'emprunts_des_livres': emprunts_des_livres})


def details_livre(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    return render(request, 'bibliotheque/details_livre.html', {'livre': livre})


@login_required
def emprunter_livre(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    if request.method == 'POST':
        date_retour = request.POST.get('date_retour')
        emprunt = Emprunt(utilisateur=request.user, livre=livre, date_retour=date_retour)
        emprunt.save()
        return HttpResponseRedirect(reverse('bibliotheque:liste_livres'))
    return render(request, 'bibliotheque/emprunter_livre.html', {'livre': livre})
