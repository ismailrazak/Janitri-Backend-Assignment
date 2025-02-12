from django.urls import path
from . import views
urlpatterns = [
    path("register/",views.RegisterView.as_view()),
    path("patients/",views.PatientView.as_view()),
    path("patients/<int:pk>",views.PatientDetailView.as_view()),
    path("heartdata/",views.HeartDataView.as_view()),
    path("heartdata/<int:pk>",views.HeartDataDetailView.as_view())

]