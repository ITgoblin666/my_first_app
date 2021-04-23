"""Опеределение URL схемы для my_app"""

from django.urls import path

from . import views

app_name = 'my_app'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех тем
    path('tems/', views.tems, name='tems'),
    # Страница с подробной информацией по теме
    path('tems/<int:tema_id>/', views.tema, name='tema'),
    # Страница с добавлением новой темы
    path('new_topic/', views.new_tema, name='new_tema'),
    # Страница для добавления новой записи
    path('new_razdel/<int:tema_id>/', views.new_razdel, name='new_razdel'),
    # Страница для редактирования записи
    path('edit_razdel/<int:razdel_id>/', views.edit_razdel, name='edit_razdel'),
]
