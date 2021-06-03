from django.urls import path

from . import views

urlpatterns = [
    path("", views.all_ppd, name="get-all-ppd"),
    path("<slug:unique_id>", views.ppd_by_id, name="get-ppd-by-id"),
    path("from/<str:from_period>/until/<str:until_period>", views.all_ppd_in_period, name="get-all-ppd-in-period"),
]
