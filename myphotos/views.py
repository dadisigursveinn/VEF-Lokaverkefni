from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})

def list(request):
    title = "My Title"

	form = PhotoForm(request.POST or None)
    
	context = {
		"title": title,
		"form": form
	}
    # Handle file upload
    if form.is_valid():
    	instance = form.save(commit=False)
    	instance.save()
    	return HttpResponseRedirect(reverse('ljosmyndasida.myphotos.views.list'))

    # Render list page with the documents and the form
    return render(request, "list.html", context)
