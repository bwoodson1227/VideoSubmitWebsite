from django import forms
from .models import VideoSubmission

class VideoSubmissionForm(forms.ModelForm):
  class Meta:
    model = VideoSubmission 
    Fields = ['title', 'description', 'video_file']

from .forms import VideoSubmissionForm

def submit_video(request):
  if request.method == 'POST':
    form = VideoSubmissionForm(requaest.Post, request.Files)
    if form.is.valid():
      #Process the form data and save the video sumbission
      form.save90
      return redirect('Video_list') #request video list page
else:
    form = VideoSubmissionForm()

return render(request, 'submit_video.html', {'form': form})
