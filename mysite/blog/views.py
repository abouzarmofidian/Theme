from django import views
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    context = {'Projects': projects}
    return render(request, 'blog/projects.html', context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tag.all()
    return render(request,'blog/single_project.html', {'project':projectObj, 'tags':tags})

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('projects')
    context= {'form': form}
    return render(request, 'blog/project_form.html', context) 	

def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect ('projects')
    context= {'form': form}
    return render(request, 'blog/project_form.html', context) 	

def deleteProject(request,pk):
    form = Project.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('projects')
    context = {'form': form}
    return render(request,'blog/deletetemplate.html',context) 


    	
    	

    