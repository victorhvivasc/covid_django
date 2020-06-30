from django.shortcuts import render
from .models import Actividades, Normativa
import request


# Create your views here.
def home(request):
    actividades = Actividades.objects.all()
    normas = Normativa.objects.all()
    provincia_list = set([])
    actividades_list = []
    lista_provincias = []
    lista_actividades = []
    post = ''
    for x in normas:
        provincia_list.add(x.provincia)
    for y in actividades:
        actividades_list.append(y.actividad)
    if request.method == 'POST':
        if 'select2' in str(request.POST):
            post = request.POST['select2']
            actividad_select = Actividades.objects.filter(actividad=post)
            #actividad_select = Actividades.select().where(Actividades.actividad == request.form['select2'])
            for c in actividad_select:
                normativa_vinculada = Normativa.objects.filter(norma=c.normativa)
                #normativa_vinculada = Normativa.select().where(Normativa.norma == c.normativa).order_by(
                #    Normativa.provincia)
                for v in normativa_vinculada:
                    provincia_habilitada = v.provincia
                    lista_provincias.append(v)
        else:
            post = request.POST['select']
            # print(request.form['select'])
            normativa_select = Normativa.objects.filter(provincia=post)
            #normativa_select = Normativa.select().where(Normativa.provincia == request.form['select'])
            for c in normativa_select:
                actividad_vinculada = Actividades.objects.filter(normativa=c.norma)
                #actividad_vinculada = Actividades.select().where(Actividades.normativa == c.norma).order_by(
                #    Actividades.actividad)
                for v in actividad_vinculada:
                    actividad_vinculada = v.actividad
                    lista_actividades.append(v)
    provincia_list = list(provincia_list)
    provincia_list.sort()
    actividades_list.sort()

    return render(request, template_name='actividades/index.html',
                  context={'actividades':actividades_list, 'provincias':provincia_list,
                           'actividades2': lista_actividades, 'provincias2': lista_provincias, 'post':post})
