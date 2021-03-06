from django.urls import path
from .views import GET_Manage_Canteens_Id_View, index_view, GET_Canteens_View, \
    GET_Categories_View, GET_Dishes_View, POST_Category_View,PATCH_Category_View,DELETE_Category_View, \
    POST_Dish_View,PATCH_Dish_View, DELETE_Dish_View, test_template, GET_all_Dishes_View

urlpatterns = [
    path('index/', index_view),

    path('get_manage_canteens/', GET_Manage_Canteens_Id_View),
    path('get_canteens/', GET_Canteens_View),
    path('get_categories/', GET_Categories_View),
    path('get_dishes/', GET_Dishes_View),
    path('get_all_dishes/', GET_all_Dishes_View),
    path('post_categories/', POST_Category_View),
    path('patch_categories/', PATCH_Category_View),
    path('delete_categories/', DELETE_Category_View),
    path('post_dish/', POST_Dish_View),
    path('patch_dish/', PATCH_Dish_View),
    path('delete_dish/', DELETE_Dish_View),
    path('test11/', test_template),
    path('', index_view),
]