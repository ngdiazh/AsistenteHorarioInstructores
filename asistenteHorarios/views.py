from django.shortcuts import render
from django.http import HttpResponse
from asistenteHorarios.FuncSprint1.Sena10 import sena10
from asistenteHorarios.FuncSprint1.Sena15 import sena15
from asistenteHorarios.models import Horario_Instructor, Instructores, Contratacion
from datetime import datetime, timedelta

def prueba(request):
    instructor = Instructores.objects.filter(id = 6) 
    consultaHorasMensualFormacion = Contratacion.objects.filter(id_Instructor = instructor[0]) 
    HorasMensualFormacion = consultaHorasMensualFormacion[0].horasMensualFormacion
    fechaInicio = datetime(2021,11,1)             # suponiendo meses el inicio como la fecha de inicio
    fechaFin = datetime(2021,11,30,23) 
    resultado = sena10(instructor, fechaInicio, fechaFin)
    durDias = resultado.total_seconds()/(3600*24)
    durHoras = resultado.total_seconds()/3600
    fichasActivas = sena15()
    ctx = {"Resultado":resultado, "DuracionDias":durDias, "DuracionHoras":durHoras, "FichasActivas":fichasActivas}
    return render(request, 'prueba.html', ctx)
