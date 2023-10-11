from main import models
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        models = models.City
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(read_only=True, slug_field='title')
    class Meta:
        model = models.User
        exclude = ['user_permissions', 'groups', 'is_superuser', 'is_staff', 'is_active', 'last_login', 'password']


class HelplessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Helpless
        fields = '__all__'


class HelplessMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HelplessMedia
        fields  = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = '__all__'


class BlogMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogMedia
        fields = ['image', 'id']


class HelpTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HelpType
        fields = '__all__'

