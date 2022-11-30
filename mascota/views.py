from django.shortcuts import render, redirect
from .forms import PublicarForm
from mascota.models import Mascota
# Create your views here.

def index(request):
    ultimas_mascotas = Mascota.objects.all().order_by('-id')[:6]

    slider = []
    slider.append(ultimas_mascotas[:3])
    slider.append(ultimas_mascotas[3:])
        
    print(slider)

    mascotas = {
        'mascotas':ultimas_mascotas,
        'slider': slider
    } 
    
    return render(request, template_name='mascota/index.html', context=mascotas)


def detalle(request, id):
    mascota = {'mascota': Mascota.objects.get(id=id)}
    return render(request, template_name='mascota/detalle.html', context=mascota)


def publicar(request):
    if request.method == 'POST':
        print(request.POST)
        form = PublicarForm(request.POST, request.FILES)
        if form.is_valid():
            mascota = form.save()
            return redirect('detalle', id=mascota.id)
        print(form.errors)
    else:
        form = PublicarForm()
    return render(request, template_name='mascota/publicar.html', context={'form': form})


def adoptar(request):
    context = {
                'mascotas': Mascota.objects.all()
            }
    
    return render(request, template_name='mascota/adoptar.html', context=context)


def register(request):
    return render(request, template_name='mascota/register.html')

