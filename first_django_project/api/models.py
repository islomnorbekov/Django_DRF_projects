from tastypie.resources import ModelResource
from .authentication import CustomAuthentication
from tastypie.authorization import Authorization
from shop.models import Category, Course


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allow_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allow_methods = ['get', 'post', 'put', 'delete']
        excludes = ['created_at', 'reviews_qty']
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return super().hydrate(bundle)

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return super().dehydrate(bundle)

    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()
