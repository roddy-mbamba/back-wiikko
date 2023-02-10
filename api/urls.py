
from django.urls import path
from api.Controllers.UserViewsSet import UserViewsSet,LoginViewsSet
from api.Controllers.MessageViewsSet import MessageViewsSet

urlpatterns = [
    path('login', LoginViewsSet.as_view()),
    path('users', UserViewsSet.as_view()),
     path('messages/<str:user_envoyer>', MessageViewsSet.as_view()),
]