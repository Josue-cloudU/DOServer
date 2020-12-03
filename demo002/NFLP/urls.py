from django.urls import path
from django.contrib.auth import views as auth_views


from NFLP import views
app_name = "NFLP"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),

    path('listjugadores/', views.ListJugador.as_view(), name="listjugadores"),
    path('detailjugador/<int:pk>/', views.DetailJugador.as_view(), name="detailjugador"),
    path('updatejugador/<int:pk>/', views.UpdateJugador.as_view(), name="updatejugador"),

    path('listequipo/', views.ListEquipo.as_view(), name="listequipo"),
    path('detailequipo/<int:pk>/', views.DetailEquipo.as_view(), name="detailequipo"),
    path('updateequipo/<int:pk>/', views.UpdateEquipo.as_view(), name="updateequipo"),

    path('listestadio/', views.ListEstadio.as_view(), name="listestadio"),
    path('detaiestadio/<int:pk>/', views.DetailEstadio.as_view(), name="detailestadio"),
    path('updateestadio/<int:pk>/', views.UpdateEstadio.as_view(), name="updateestadio"),
]
