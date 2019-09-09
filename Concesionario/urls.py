
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from concesionarioapp.views import Login
from concesionarioapp.views import Logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Login.as_view(), name='login'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^vendedores/', include(('vendedores.urls', 'vendedores'), namespace='vendedores')),
    url(r'^compradores/', include(('compradores.urls', 'compradores'), namespace='compradores')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
