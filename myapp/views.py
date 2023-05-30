from django.shortcuts import render, redirect
from myapp.models import *
from myapp.forms import *
from django.shortcuts import get_object_or_404
from django.db import connection




def process_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result



def departement_list(request):
    departements = Departement.objects.all()
    return render(request, 'departement_list.html', {'departements': departements})

def employe_list(request):
    employes = Employe.objects.all()
    return render(request, 'employe_list.html', {'employes': employes})


def agenda_list(request):
    agendas = Agenda.objects.all()
    return render(request, 'agenda_list.html', {'agendas': agendas})

def home(request):
    return render(request, 'home.html')

def procesverbal_list(request):
    procesverbals = ProcesVerbal.objects.all()
    return render(request, 'procesverbal_list.html', {'procesverbals': procesverbals})

def activitesdept_list(request):
    activitesdepts = ActivitesDept.objects.all()
    return render(request, 'activitesdept_list.html', {'activitesdepts': activitesdepts})

def actdeptverbal_list(request):
    actdeptverbals = ActDeptVerbal.objects.all()
    return render(request, 'actdeptverbal_list.html', {'actdeptverbals': actdeptverbals})

def absent_list(request):
    absents = Absent.objects.all()
    return render(request, 'absent_list.html', {'absents': absents})

def activites_list(request):
    activites = Activites.objects.all()
    return render(request, 'activites_list.html', {'activites': activites})

def alertes_list(request):
    alertes = Alertes.objects.all()
    return render(request, 'alertes_list.html', {'alertes': alertes})

def add_departement(request):
    if request.method == 'POST':
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departement_list')
    else:
        form = DepartementForm()
    return render(request, 'add_departement.html', {'form': form})



def add_agenda(request):
    if request.method == 'POST':
        
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda_list')
    else:
        form = AgendaForm()
    return render(request, 'add_agenda.html', {'form': form})








def add_employe(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employe_list')
    else:
        form = EmployeForm()
    return render(request, 'add_employe.html', {'form': form})




def employe_update(request, id):  
    employe = Employe.objects.get(numEmploye=id)
    form = EmployeForm(initial={'num': employe.numEmploye, 'nom': employe.nom, 'Prenom': employe.prenom, 'tel': employe.telIntern, 'email': employe.email, 'niveau': employe.niveau, 'Departement': employe.numDept})
    if request.method == "POST":  
        form = EmployeForm(request.POST, instance=employe)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('employe_list')  
            except Exception as e: 
                pass    
    return render(request,'employe_update.html',{'form':form})  



def employe_delete(request, id):
    employe = Employe.objects.get(numEmploye=id)
    try:
        employe.delete()
    except:
        pass
    return redirect('employe_list')


def execute_query(request):
    context = {}
    if request.method == 'POST':
        query = request.POST.get('query')
        with connection.cursor() as cursor:
            # Handle queries that modify the database
            if query.strip().lower().startswith(('insert', 'update', 'delete')):
                cursor.execute(query)
                context['query'] = query
                context['execution_success'] = True
            else:
                # Handle queries that retrieve data
                cursor.execute(query)
                result = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                context = {
                    'query': query,
                    'result': result,
                    'columns': columns,
                }

    return render(request, 'script.html', context)





def script_page(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        # Process the query and get the result
        result = process_query(query)
        return render(request, 'script.html', {'result': result})
    return render(request, 'script.html')



def add_activites(request):
    if request.method == 'POST':
        form = ActivitesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activites_list')
    else:
        form = ActivitesForm()
    return render(request, 'add_activites.html', {'form': form})




def activites_update(request, id):  
    activites = Activites.objects.get(numActivite=id)
    form = ActivitesForm(initial={'num': activites.numAct, 'nom': activites.typeA, 'Prenom': activites.description, 'tel': activites.dateAct, 'email': activites.hDebut, 'niveau': activites.hFin, 'Departement': activites.dateCreation,  'Departement': activites.createur, 'Departement': activites.visible, 'Departement': activites.numAgenda})
    if request.method == "POST":  
        form = ActivitesForm(request.POST, instance=employe)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('activites_list')  
            except Exception as e: 
                pass    
    return render(request,'activites_update.html',{'form':form})  



def activites_delete(request, id):
    activites = Activites.objects.get(numEmploye=id)
    try:
        activites.delete()
    except:
        pass
    return redirect('activites_list')




def departement_update(request, id):  
    departement = Departement.objects.get(num=id)
    form = DepartementForm(initial={'nom': departement.num, 'nom': departement.nom, 'Chef': departement.numChef, 'Agenda': departement.numAgendaDept})
    if request.method == "POST":  
        form = DepartementForm(request.POST, instance=departement)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('departement_list')  
            except Exception as e: 
                pass    
    return render(request,'departement_update.html',{'form':form})  



def departement_delete(request, id):
    departement = Departement.objects.get(num=id)
    try:
        departement.delete()
    except:
        pass
    return redirect('departement_list')
