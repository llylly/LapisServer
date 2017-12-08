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
import userapp.views

urlpatterns = [
    url(r'^about$', mainapp.views.about),
    url(r'^examples$', mainapp.views.examples),
    url(r'^tutorial$', mainapp.views.tutorial),
    url(r'^index_fileupload$', mainapp.views.index_fileupload),
    url(r'^get_cloud_api_examples$', mainapp.views.get_cloud_api_examples),
    url(r'^download_cloud_api_examples$', mainapp.views.download_cloud_api_examples),
    url(r'^read_cloud_api_examples$', mainapp.views.read_cloud_api_examples),

    url(r'^api/session_verify$', coreapp.views.session_verify),
    url(r'^api/script_parse$', coreapp.views.script_parse),
    url(r'^api/script_transform$', coreapp.views.script_transform),
    url(r'^api/script_download$', coreapp.views.script_download),
    url(r'^api/apidata_gen$', coreapp.views.apidata_gen),
    # url(r'^api/single_test$', coreapp.views.single_test),
    # url(r'^api/scenario_test$', coreapp.views.scenario_test),
    # url(r'^api/scenario_test_query$', coreapp.views.scenario_test_query),

    url(r'^api/user/register$', userapp.views.register),
    url(r'^api/user/login$', userapp.views.login),
    url(r'^api/user/get_status$', userapp.views.get_status),
    url(r'^api/user/logout$', userapp.views.logout),
    url(r'^api/user/change_passwd$', userapp.views.change_passwd),
    url(r'^api/user/get_filelist$', userapp.views.get_filelist),
    url(r'^api/user/load_file$', userapp.views.load_file),
    url(r'^api/user/save_file$', userapp.views.save_file),
    url(r'^api/user/rename_file$', userapp.views.rename_file),
    url(r'^api/user/del_file$', userapp.views.del_file),
    url(r'^api/user/file_import$', userapp.views.file_import),
    url(r'^api/user/clean_all$', userapp.views.clean_all),
    url(r'^api/user/make_download_all$', userapp.views.make_download_all),
    url(r'^api/user/download_all$', userapp.views.download_all),

    url(r'^$', mainapp.views.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
