from rest_framework import serializers, permissions
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# instead using serializers.Serializer, use ModelSerializer instead to avoid copy/pasting code from the models class
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')

# represents the users added with createsuperuser
class UserSerializer(serializers.ModelSerializer):
    # snippets not included by default when using ModelSerializer
    # since snippets is a reverse relationship on the User model.
    # Solution is to add an explicit field for it here
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')