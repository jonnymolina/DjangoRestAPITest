from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from snippets.permissions import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import 
from rest_framework.decorators import detail_route

# This ViewSet replaced SnippetList, SnippetDetail, SnippetHighlight
# ModelViewSet - gets complete set of default read and write operations
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # @detail_route used to create a custom action, named 'highlight'
    # this decorator can be used to add any custom endpoints that don't
    # fit into the standard create/update/delete style
    # Custom actions using detail_route responds to GET requests.
    # We can use the 'methods' argument if we wanted an action that
    # responded to POST requests.
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# This ViewSet replaced UserList and UserDetail
# ReadOnlyModelViewSet - provides default 'read-only' operations
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    # this is like before in the old views
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        # reverse used to return fully-qualified URLs
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })