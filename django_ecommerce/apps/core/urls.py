from django.urls import path


from . import views


urlpatterns=[

    path('',views.frontpage, name='frontpage'),
    path('contact/',views.contact, name='contact'),
    path('about_project', views.about_project, name='about_project'),
]

handler404='apps.core.views.error_404_view'