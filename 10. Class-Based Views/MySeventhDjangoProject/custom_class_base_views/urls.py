from django.urls import path

from MySeventhDjangoProject.custom_class_base_views.views import index
from MySeventhDjangoProject.web.views import IndexView

urlpatterns = (
    path("", index, name="ccbc_index"),
    path("cbv/", IndexView.as_view(), name="ccbc_cbv_index"),
)