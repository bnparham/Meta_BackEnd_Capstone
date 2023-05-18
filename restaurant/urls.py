from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemView

urlpatterns = [
    path("", index.as_view(), name="index"),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]
