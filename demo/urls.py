from django.urls import path, include

from demo.swagger_schema import SwaggerSchemaView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('cbv/', include('demo.cbv_demo.urls')),
    path('fbv/', include('demo.fbv_demo.urls')),
    path('swagger/', SwaggerSchemaView.as_view()),
]
