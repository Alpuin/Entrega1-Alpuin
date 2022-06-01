from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('personal/', views.staffs, name='Staffs'),
    path('proyectos/', views.projects, name='Projects'),
    path('productos/', views.products, name='Products'),
    path('personal-formulario/', views.staffs_forms, name='StaffsForms'),
    path('proyectos-formulario/', views.projects_forms, name='ProjectsForms'),
    path('productos-formulario/', views.products_forms, name='ProductsForms'),
    # path('busqueda/', views.search, name='Search')
]