from  django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ViewSets', TodosViewSetApiView)


urlpatterns = [
    path('', Index, name='index_page'),
    # path('todo-json/', todo_json, name='todo_json_page'),
    # path('todo-w-serializer/', all_todos_w_serializer, name='all_todos_w_serializer'),
    # path('todo-detail/<int:todo_id>', todo_detail_view, name='todo_detail_page'),

    # path('cbv/', TodosListApiView.as_view(), name='manage-todo'),
    # path('cbv/<int:todo_id>', TodosDetailApiView.as_view(), name='manage-todo'),

    #! MixIns
    path('mixins/', TodosListMixinApiView.as_view(), name='mixins'),
    path('mixins/<pk>', TodosDetailMixinApiView.as_view(), name='mixins_detail'),

    #? Generics
    path('generics/' , TodosGenericApiView.as_view()) ,
    path('generics/<pk>' , TodosDetailGenericApiView.as_view()),

    #* ViewSets
    #!Note: you can declare path here or on top inside register, prefix
    path('', include(router.urls))

]