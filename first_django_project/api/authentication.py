from tastypie.authentication import ApiKeyAuthentication


class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True

        # Custom authentication logic
        return super().is_authenticated(request, **kwargs)
