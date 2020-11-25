from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('', include('home.urls')),
    path('', include('administrator.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('members/',  include('member.urls')),
    path('shares/',  include('share.urls')),
    path('loans/',  include('loan.urls')),
    path('balance/',  include('balance.urls')),
    path('report/',  include('report.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
