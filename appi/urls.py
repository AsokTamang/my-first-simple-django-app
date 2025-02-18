from django.urls import path
from . import views 
urlpatterns= [path('',views.base,name='base')
            ,path('add',views.add,name='add'),
             path('update',views.update,name='update'),
             path('updation/<int:id>',views.updation,name='updation'),
             path('delete',views.delete,name='delete'),
             path('success/<str:x>',views.success,name='success'),
             path('delete',views.delete,name='delete'),
             path('deletion/<int:id>',views.deletion,name='deletion'),
             path('yes/<int:id>',views.yes,name='yes'),
             path('no',views.no,name='no')
                  ]
