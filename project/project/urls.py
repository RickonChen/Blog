"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from . import settings
from base import views
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('accounts/register/', views.Register.as_view(), name='register'),
    path('accounts/change/<int:pk>/', views.UserChange.as_view(), name='user_change'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('base.urls')),
    path('blog/', include('blog.urls')),
    path('tags/<slug:slug>/', views.tag, name='tag'),
    path('search/', include('search.urls')),
    path('about/', views.about, name='about'),
    prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
