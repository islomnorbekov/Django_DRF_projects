from django.urls import path, include
from api.models import CategoryResource, CourseResource
from tastypie.api import Api

# examplyary of how to use the API resources in the urls.py file

api = Api(api_name='v1')
course_resource = CourseResource()
category_resource = CategoryResource()
api.register(course_resource)
api.register(category_resource)

urlpatterns = [
    path('', include(api.urls), name='index'),
]
