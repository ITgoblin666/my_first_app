from django.shortcuts import render, redirect

from .models import Tema, Razdel
from .forms import TemaForm, RazdelForm


def index(request):
    """Домашняя страница приложения My Site"""
    return render(request, 'my_app/index.html')


def tems(request):
    """Выводит список всех тем"""
    tems = Tema.objects.order_by('date_added')
    context = {'tems': tems}
    return render(request, 'my_app/tems.html', context)


def tema(request, tema_id):
    """Выводит одну тему и все ее записи."""
    tema = Tema.objects.get(id=tema_id)
    razdely = tema.razdel_set.order_by('-date_added')
    context = {
        'tema': tema,
        'razdely': razdely
    }
    return render(request, 'my_app/tema.html', context)


def new_tema(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        form = TemaForm()
    else:
        form = TemaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:tems')

    context = {'form': form}
    return render(request, 'my_app/new_tema.html', context)


def new_razdel(request, tema_id):
    """Добавляет новую запись по конкретной теме"""
    tema = Tema.objects.get(id=tema_id)
    if request.method != 'POST':
        form = RazdelForm()
    else:
        form = RazdelForm(data=request.POST)
        if form.is_valid():
            new_razdel = form.save(commit=False)
            new_razdel.tema = tema
            new_razdel.save()
            return redirect('my_app:tema', tema_id=tema_id)

        # Вывести пустую или недействителную форму.
    context = {'tema': tema, 'form': form}
    return render(request, 'my_app/new_razdel.html', context)


def edit_razdel(request, razdel_id):
    """Редактирует существующую запись."""
    razdel = Razdel.objects.get(id=razdel_id)
    tema = razdel.tema

    if request.method != 'POST':
        form = RazdelForm(instance=razdel)
    else:
        form = RazdelForm(instance=razdel, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:tema', tema_id=tema.id)

    context = {'razdel': razdel, 'tema': tema, 'form': form}
    return render(request, 'my_app/edit_razdel.html', context)
