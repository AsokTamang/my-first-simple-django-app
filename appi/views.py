#this is the backend
from django import forms
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpRequest
from .models import players
from .forms import playerform,playeridform

from django.template import loader 
def base(request):
   return render(request,'base.html')
   
   
def add(request):
   f=playerform() 
   if request.method=='POST':
    f=playerform(request.POST) #this code helps to add the datas input by the user and pass it to the server 
    if f.is_valid():
       f.save()
       return redirect('success',x='addition')
    else:
       return render(request,'add.html',{'f':f})    
   return render(request,'add.html',{'f':f}) 


def update(request):
   f=playeridform()
   if request.method=='POST':
    f=playeridform(request.POST)
    if f.is_valid():
       player_id=f.cleaned_data['id']#here f.cleaned_data is an attribute of a form that cleans the data 
       try:
          total_players=players.objects.get(id=player_id)
          return redirect('updation',id=player_id)
       except players.DoesNotExist:
          #here players.DoesNotExist is the method of model which checks if the data exist or not 
         return render(request,'donot2.html')
   return render(request,'update.html',{'f':f})
       


    
   
def updation(request,id):
    a=get_object_or_404(players,id=id)
    f=playerform(instance=a)#here, instance=a means retrieving the form of a player according to the id input by the user
    if request.method=='POST':
     f=playerform(request.POST,instance=a)
     if f.is_valid():
        f.save()
        return redirect('success',x='updation')
     
    else:
       return render(request,'updation.html',{'f':f})
        
def success(request,x):
  return render(request,'success.html',{'x':x})      
def delete(request):
   a=playeridform()
   if request.method=='POST':
      a=playeridform(request.POST)
      if a.is_valid():
         b=a.cleaned_data['id']
        
         return redirect('deletion',id=b)
        
   return render(request,'delete.html',{'a':a})

def deletion(request,id=id):
   try:
      a=players.objects.get(id=id)
      return render(request,'deletion.html',{'a':a})
   except players.DoesNotExist:
      return render(request,'donot.html')
def yes(request,id):
   a=players.objects.get(id=id)
   a.delete()
   return redirect('success',x='Deletion')
def no(request):
   return redirect('delete')   

         






