from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [

    #Examples:
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),

]