from rest_framework import serializers

from .models import Category, Product, File


class CategorySerializer(serializers.ModelSerializer):
    back = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'avatar', 'url', 'back')
    
    def get_back(self, obj):
        return 'http://127.0.0.1:8000/categories/'


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ('id', 'product','title', 'file', 'file_type')

    def get_file_type(self, obj):
        return obj.get_file_type_display()


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)
    back = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'avatar', 'categories', 'files', 'url', 'back')

    def get_back(self, obj):
        return 'http://127.0.0.1:8000/products/'

