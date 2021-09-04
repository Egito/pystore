from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pce001.urls')),
    path('', include('acessos.urls')),
    path('produtos/', include('products.urls')),
    path('carrinho/', include('pvd001.urls')),
    path('parcelas/', include('parcels.urls')),
    path('eventos/', include('eventos.urls')),
    path('radios/', include('radios.urls')),
    path('admin/', admin.site.urls),
    path('upload/', include('myapp.urls')),
]

#if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    