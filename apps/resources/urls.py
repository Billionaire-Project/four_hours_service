from django.urls import path

from apps.resources.views import resource_topic


urlpatterns = [
    path("topic/", resource_topic.ResourceTopic.as_view(), name="resource_topic"),
]
