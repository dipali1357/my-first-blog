from django.shortcuts import render
from rango.models import Category

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}
	return render(request, 'rango/index.html', context_dict)

def contents(request):
	context_dict = {'boldmessage' : "Crunchy,cookie,creamy,candy,cupake!"}
	return render(request,'rango/contents.html',context=context_dict)

def about(request):
	return render(request,'rango/about.html',{'aboutme':"It is website containing various categories and pages"})