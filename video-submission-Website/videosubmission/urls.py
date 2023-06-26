# Url patterns
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

#url patterns for HTML
from django.urls import is_valid_path
from videosubmission import views

urlpatterns = [
    path('submit/', views.submit_video, name='submit_video'),
]

from django.conf import settings
from django.conf.urls.static import static


#after the url patterns list

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import is_valid_path
from . import views

urlpatterns = [
    path('submit/', views.submit_video, name='submit_video'),
    path('success/', views.success_page, name='success'), #add this line for the success page
    ]