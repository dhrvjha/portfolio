from django.urls import path, include

urlpatterns: list = [
    path("discover/", include("portfolio.discovery.urls")),
    path("create/", include("portfolio.creator.urls"))
]
