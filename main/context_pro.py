from .models import * 

def view_all(request):
	context = {
		'creators':Creator.objects.all(),
	}
	return context