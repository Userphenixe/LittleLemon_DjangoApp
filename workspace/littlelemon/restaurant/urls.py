from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view(), name='MenuItemsView'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name = 'SingleMenuItemView'),
    path('api-token-auth/', obtain_auth_token),
]