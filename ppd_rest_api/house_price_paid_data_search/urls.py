from django.urls import path

from . import views

urlpatterns = [
    path("",views.all_ppd),
    path("<slug:unique_id>",views.ppd_by_id),
    path("from/<str:from_period>/until/<str:until_period>",views.all_ppd_in_period),
]