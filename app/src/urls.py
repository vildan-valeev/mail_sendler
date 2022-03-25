from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from src.settings.components.base import PROJECT_NAME

urlpatterns = [
    path('polls/', include('mail.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = PROJECT_NAME
admin.site.site_title = PROJECT_NAME
admin.site.index_title = f"Добро пожаловать в {PROJECT_NAME}"
