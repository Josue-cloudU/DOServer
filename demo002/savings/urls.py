from django.urls import path

from savings import views
app_name = "savings"

urlpatterns = [
    path('indexs/', views.Index.as_view(), name="indexs"),
    path('list_users/', views.ListUsers.as_view(), name="list_users"),
    path('user_lists/', views.list_Users, name="user_lists"),
    path('list_saving/', views.ListSaving.as_view(), name="list_saving"),
    path('saving_list/', views.list_Saving, name="saving_list"),
    path('saving_create/', views.SavingCreate.as_view(), name="saving_create"),
    path('create_saving/', views.createCundina, name="create_saving"),

    path('user_creates/', views.UserCreate.as_view(), name="user_creates"),
    path('create_users/', views.createUser, name="create_users"),
]
