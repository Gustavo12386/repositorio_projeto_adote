from django.shortcuts import render
from divulgar.models import Pet, Raca
from adotar.models import PedidoAdocao
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect
import datetime

def listar_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status="P")
        racas = Raca.objects.all()
        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')

        if cidade:
            pets = pets.filter(cidade__icontains=cidade)
        if raca_filter:
            pets = pets.filter(raca__id=raca_filter) 
            raca_filter = Raca.objects.get(id=raca_filter)   
        return render(request, 'listar_pets.html', {'pets': pets, 'racas': racas, 'cidade': cidade, 'raca_filter': raca_filter})

def ver_pet(request, id):
    if request.method == "GET":
        pet = Pet.objects.get(id = id)
        return render(request, 'ver_pet.html', {'pet': pet})    

def pedido_adocao(request, id_pet):
    pet = Pet.objects.filter(id=id_pet).filter(status="P")

    pedido = PedidoAdocao(pet=pet.first(),
                          usuario=request.user,
                          data=datetime.datetime.now())

    pedido.save()

    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção realizado, você receberá um e-mail caso ele seja aprovado.')
    if not pet.exists():
        messages.add_message(request, constants.ERROR, 'Esse pet já foi adotado :)')
        return redirect('/adotar')
    return redirect('/adotar')     
    




