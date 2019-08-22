from django.conf.urls import url
from django.contrib import admin
from main import views
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  path('graphql/',csrf_exempt(GraphQLView.as_view(graphiql=True)))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

