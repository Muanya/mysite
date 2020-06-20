from django.shortcuts import render


def resume_index(request):
	contxt = {
		'title': 'My Resume',
	}

	return render(request, 'resume_index.html', contxt)