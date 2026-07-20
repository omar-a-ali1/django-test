import pandas as pd
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ECGInputSerializer, TaskSerializer
from .models import Task
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .helper import (
    scaler, knn_model, dt_model, rf_model, svm_model, xgboost_model
)


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


ECG_FEATURES = ['RR', 'PR', 'QRS', 'QT', 'Amp_R', 'Amp_P', 'Amp_T']

MODELS = {
    'knn': knn_model,
    'decision_tree': dt_model,
    'random_forest': rf_model,
    'svm': svm_model,
    'gradient_boosting': xgboost_model,
}


class PredictECG(APIView):
    def post(self, request):
        serializer = ECGInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        features = pd.DataFrame([[data[f] for f in ECG_FEATURES]], columns=ECG_FEATURES)
        scaled = scaler.transform(features)

        model_name = request.query_params.get('model', 'random_forest')
        model = MODELS.get(model_name)
        if model is None:
            return Response(
                {'error': f"Unknown model '{model_name}'. Choose from: {list(MODELS.keys())}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        prediction = int(model.predict(scaled)[0])

        return Response({
            'model': model_name,
            'prediction': prediction,
            'input': data,
        })
