from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from . import optimiser
from . import models
context = {'a':"a",'b':" + b",'c':" + c",'d':" + d",'x1':"", 'x2':"", 'x3':""}
# Create your views here.
def index(request):
	equation = models.Equation()
	if request.method =="POST":
		a=request.POST.get("a")
		if(float(a)==1):a=''
		b=request.POST.get("b")
		if(float(b)>=0):
			if(b==1):b=''
			else:b = " + " + b
		c=request.POST.get("c")
		if(float(c)>=0):
			if(c==1):c=''
			else:c = " + " + c
		d=request.POST.get("d")
		if(float(d)>=0): d = " + " + d
		roots = optimiser.calculation(float(request.POST.get("a")), float(request.POST.get("b")), float(request.POST.get("c")),float(request.POST.get("d")))
		equation.a=request.POST.get("a")
		equation.b=request.POST.get("b")
		equation.c=request.POST.get("c")
		equation.d=request.POST.get("d")
		koef=(a,b,c,d)
		equation.x1=str(roots[0])
		equation.x2=str(roots[1])
		equation.x3=str(roots[2])
		korni=(equation.x1, equation.x2, equation.x3)
		equation.save()
		
		res = float(request.POST.get("a"))*roots[0]**3+float(request.POST.get("b"))*roots[0]**2+float(request.POST.get("c"))*roots[0]+float(request.POST.get("d")),float(request.POST.get("a"))*roots[1]**3+float(request.POST.get("b"))*roots[1]**2+float(request.POST.get("c"))*roots[1]+float(request.POST.get("d")),float(request.POST.get("a"))*roots[2]**3+float(request.POST.get("b"))*roots[2]**2+float(request.POST.get("c"))*roots[2]+float(request.POST.get("d")) 
		global context
		context={'a':a,
					 'b':b,
					 'c':c,
					 'd':d,
					 'x1':roots[0],
					 'x2':roots[1], 
					 'x3':roots[2],
					 'res1':res[0],
					 'res2':res[1],
					 'res3':res[2]}
		print(type(roots))
		return redirect('base:main')
	if(request.method=="GET"):
		return render(request,'base/base.html', context)
	
