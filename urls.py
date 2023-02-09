from src.urls import Url
from views import Home


urlpatterns = [
    Url(r'/', Home),
    Url('/favicon.ico', Home)
]


