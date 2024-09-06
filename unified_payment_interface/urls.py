from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('api/user/', include("accounts.urls")),
    path('api/user/upi/', include("upi_ids.urls")),
    path('api/user/transactions/', include("transactions.urls")),  # Ensure transactions URLs are included
    re_path(r"^favicon\.ico$", RedirectView.as_view(url="/static/images/favicon.ico")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
