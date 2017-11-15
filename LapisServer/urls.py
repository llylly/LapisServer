"""LapisServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
import settings
import mainapp.views
import coreapp.views

urlpatterns = [
    url(r'^about$', mainapp.views.about),
    url(r'^examples$', mainapp.views.examples),
    url(r'^index_fileupload$', mainapp.views.index_fileupload),

    url(r'^api/session_verify$', coreapp.views.session_verify),
    url(r'^api/script_parse$', coreapp.views.script_parse),
    url(r'^api/apidata_gen$', coreapp.views.apidata_gen),
    url(r'^api/single_test$', coreapp.views.single_test),
    url(r'^api/scenario_test$', coreapp.views.scenario_test),
    url(r'^api/scenario_test_query$', coreapp.views.scenario_test_query),

    url(r'^', mainapp.views.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
