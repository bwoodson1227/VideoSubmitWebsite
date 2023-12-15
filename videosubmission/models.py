
from django.db import models

class Video(models.models):
    title = models.Charfield(max_length=200)
    video_file = models.FileField(upload_to'videos/')
    submitted_at = modelsDateTimeField(auto_now_add=TRUE)

    def __str__(self):
        return self.title


from django.db import models

class Video(models.models):
    title = models.Charfield(max_length=200)
    video_file = models.FileField(upload_to'videos/')
    submitted_at = modelsDateTimeField(auto_now_add=TRUE)

    def __str__(self):
        return self.title
