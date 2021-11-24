from os import stat
# Python method stat() performs a stat system call on the given path.
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myfaceapp.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




