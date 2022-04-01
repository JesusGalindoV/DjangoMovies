from django.urls import URLPattern, path
from starlink import views

urlpatterns =[
    path('', views.start, name='start'),
    path('pelicula',views.start, name='ver_peliculas'),
    path('agregar',views.agregar, name="agregar"),
    path("borrar-<int:id>", views.borrar , name="borrar"),
    path('modificar',views.agregar, name="agregar"),
    path('modificar-<int:id>',views.modificar,name="modificar"),

    path('movies', views.index, name="index"),
    
]
