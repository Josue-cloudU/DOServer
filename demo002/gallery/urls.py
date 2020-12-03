from django.urls import path

from gallery import views
app_name = "gallery"

urlpatterns = [
    path('index/', views.list_Item, name="index"),
    path('list_user/', views.ListUser.as_view(), name="list_user"),
    path('user_list/', views.list_User, name="user_list"),
    path('user_create/', views.UserCreate.as_view(), name="user_create"),
    path('create_user/', views.createUser, name="create_user"),
    path('list_new_item/', views.ListNewItem.as_view(), name="list_new_item"),
    path('list_item/', views.list_Item, name="list_item"),
    path('item_create/', views.ItemCreate.as_view(), name="item_create"),
    path('create_item/', views.createItem, name="create_item"),
    path('list_aaitem/', views.ListAAItem.as_view(), name="list_aaitem"),
    path('list_sritem/', views.ListSRItem.as_view(), name="list_sritem"),
    path('list_ritem/', views.ListRItem.as_view(), name="list_ritem"),
    path('aaitem_list/', views.list_AAItem, name="aaitem_list"),
    path('sritem_list/', views.list_SRItem, name="sritem_list"),
    path('ritem_list/', views.list_RItem, name="ritem_list"),
]
