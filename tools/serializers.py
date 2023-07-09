from rest_framework.serializers import ModelSerializer

from tools.models import SubTools, Tools


class SubToolsSerializer(ModelSerializer):
    class Meta:
        model = SubTools
        fields = ('id', 'name')


class ToolsSerializer(ModelSerializer):
    sub_tools = SubToolsSerializer(many=True, read_only=True)

    class Meta:
        model = Tools
        fields = ('id', 'name', 'sub_tools')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['sub_tools'] = SubToolsSerializer(instance.subtools_set.all(), many=True).data
        return representation
