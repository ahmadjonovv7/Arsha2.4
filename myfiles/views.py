import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import Portfolio,Murojat,team
# Create your views here.

def index(request):
    if 'text' in request.POST:
        malumot = request.POST.get('text')
        soz = str(malumot).strip()
        qidirish = Q(nomi__startswith=soz) | Q(comp_name__startswith=soz)| \
                   Q(url__startswith=soz) | Q(data__startswith=soz) | Q(text__startswith=soz)| Q(tur__nomi__startswith=soz)
        port = Portfolio.objects.filter(qidirish)
        return render(request, 'index.html', {'works': port})

    if 'name' in request.POST:
        name = request.POST.get('name')
        pochta = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        vaqt = datetime.datetime.now()
        Murojat(ism=name,pochta=pochta,sub=sub,text=msg,data=vaqt).save()
    port = Portfolio.objects.all()
    return render(request,'index.html',{'works':port})

def portfolio_detalis(request,id):
    port = Portfolio.objects.get(id=id)
    return render(request,'portfolio-details.html',{'work':port})


def Team(request):
    if 'Team' in request.POST:
        malumot = request.POST.get('text')
        soz = str(malumot).strip()
        qidirish = Q(nomi__startswith=soz) | Q(text__startswith=soz) | Q(lavozim__startswith=soz)
        port = team.objects.filter(qidirish)
        return render(request, 'index.html', {'works': port})

