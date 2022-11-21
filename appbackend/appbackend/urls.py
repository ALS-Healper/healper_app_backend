"""appbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from questionnaires import views
from users.views import UserDetailViewSet, UserViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
#User routes
router.register(r'users', UserViewSet)
router.register(r'user-detail', UserDetailViewSet, basename="user-detail")

#question routes
router.register(r'questionEntries', views.ClientEntryViewSet, basename="questionEntries")
router.register(r'questions',views.QuestionViewSet, basename="questions")
router.register(r'questionnaires', views.QuestionnaireViewSet, basename="questionnaires")

#entry routes
router.register(r'choiceentries', views.QuestionChoiceEntryViewSet, basename="choiceentries")
router.register(r'inputentries', views.QuestionInputEntryViewSet, basename="inputentries")
router.register(r'numericentries', views.QuestionNumericEntryViewSet, basename="numericentries")

#url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    #path('api/questionEntries/', views.QuestionEntryViewSet.as_view(), name="questionEntries")
]
