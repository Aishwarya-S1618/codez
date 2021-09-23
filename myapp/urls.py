from django.urls import path
from . import views

urlpatterns = [
   # path('', views.index),
    path('contact/', views.index, name='index'),
    path('', views.self, name='self'),
    path('about/', views.about, name='about'),
    path('sample/', views.sample, name='sample'),
    
]
from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
