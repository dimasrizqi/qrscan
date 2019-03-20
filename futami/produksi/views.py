from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . models import Release
# Create your views here.
def index(request):
	var_title = "List Produksi"
	var_release = Release.objects.all()
	return render(request, 'index.html', {
		'title' : var_title,
		'release' : var_release,
		})
def json(request):
	var_release = Release.objects.all()
	context = {
		'title':'judulnya JSON',
		'Description':'pemograman itu mudah',
		# 'release' : var_release,
	}

	return JsonResponse(context)

def release(request,produksi_id):
	var_release = Release.objects.filter(produksi_id=produksi_id)
	var_title = "hasil produksi"
	return render(request, 'show.html', {
		'release' : var_release,
		'title' : var_title,
		})