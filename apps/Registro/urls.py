from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [

    # listar las carreras de la bd
    path('listarCarreras', views.listar_carreras, name="listar_carreras"),

    # agregar una carrera
    path('agregar_carrera', views.agregar_carrera, name="agregar_carrera"),

    # editar una carrera
    path('editar_carrera/<int:carrera_id>', login_required(views.editar_carrera), name="editar_carrera"),

    # borrar una carrera
    path('borrar_carrera/<int:carrera_id>', login_required(views.borrar_carrera), name="borrar_carrera"),

    # llamando a la clases 
    path('add_carrera', views.CarreraCreate.as_view(), name="add_carrera"),

    path('list_carreras/', views.CarreraList.as_view(), name='list_carreras'),

    path('edit_carrera/<int:pk>', views.CarreraUpdate.as_view(), name='edit_carrera'),

    path('del_carrera/<int:pk>', views.CarreraDelete.as_view(), name='del_carrera'),

]

