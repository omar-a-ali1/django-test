from rest_framework import serializers
from .models  import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields ='__all__'


class ECGInputSerializer(serializers.Serializer):
    RR = serializers.FloatField()
    PR = serializers.FloatField()
    QRS = serializers.FloatField()
    QT = serializers.FloatField()
    Amp_R = serializers.FloatField()
    Amp_P = serializers.FloatField()
    Amp_T = serializers.FloatField()