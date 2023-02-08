from rest_framework import routers
from api.Controllers.MessageViewsSet import MessageViewsSet
from api.Controllers.UserViewsSet import UserViewsSet

rooter_url = routers.DefaultRouter()
rooter_url.register('users', UserViewsSet)
rooter_url.register('messages', MessageViewsSet)
