"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
import nuans_app.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', nuans_app.views.base, name='base'),
    path('hakk/', nuans_app.views.hakk, name='hakk'),
    path('blogs/', nuans_app.views.blogs, name='blogs'),
    path('hizmetler/', nuans_app.views.hizmetler, name='hizmetler'),
    path('iletisim/', nuans_app.views.iletisim, name='iletisim'),
    # path('jobs/<int:job_id>', jobs.views.detail, name='detail')
    
    
] \


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
