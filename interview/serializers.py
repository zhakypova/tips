from rest_framework import serializers

from .models import Category, QuestionAnswer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QASerializer(serializers.ModelSerializer):
    answer = serializers.CharField(allow_blank=True, write_only=True)

    class Meta:
        model = QuestionAnswer
        fields = '__all__'

    def validate(self, data):
        if data['importance'] < 0 or data['importance'] > 100:
            raise serializers.ValidationError('importance может быть только от 0 до 100')
        return data

class QASerializerOne(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'

    def validate(self, data):
        if data['importance'] < 0 or data['importance'] > 100:
            raise serializers.ValidationError('importance может быть только от 0 до 100')
        return data

