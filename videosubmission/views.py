from django.shortcuts import render, redirect
from .forms import VideoForm

def submit_video(request):
    if request.method == 'Post':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.submitted_by = request.user  #associate the submission
            video.save()
            return redirect('success')    #redirect to a success page
        else:
            form = VideoForm()
        
        context = {'form': form}
        return render(request, 'videosubmission/submit_video.html', context)

from django.shortcuts import render

def success_page(requests):
     return render(requests, 'videosubmission/succes.html')