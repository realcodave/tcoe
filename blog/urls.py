from django.urls import path
from .views import blog, detail
urlpatterns = [
    path('', blog, name="blog"),
    path('detail/<slug>/', detail, name="detail")
]