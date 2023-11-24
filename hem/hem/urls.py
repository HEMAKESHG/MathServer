from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofsquareprism/',views.squareprism,name="areaofsquareprism"),
    path('',views.squareprism,name="areaofsquareprismroot")
]