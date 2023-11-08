from rest_framework import viewsets

from .models import (
    ProgramMaster,
    WorkoutMaster,
    WeightedWorkoutLogMaster,
    CardioWorkoutLogMaster,
)
from .serializers import (
    ProgramMasterSerializer,
    WorkoutMasterSerializer,
    WeightedWorkoutLogMasterSerializer,
    CardioWorkoutLogMasterSerializer,
)

# Create your views here.


class ProgramMasterViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Programs.
    """

    queryset = ProgramMaster.objects.all()
    serializer_class = ProgramMasterSerializer


class WorkoutMasterViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Workouts.
    """

    queryset = WorkoutMaster.objects.all()
    serializer_class = WorkoutMasterSerializer


class WeightedWorkoutLogMasterViewSet(viewsets.ModelViewSet):
    """
    Viewset for viewing, creating, and Adding Weighted workout logs.
    """

    queryset = WeightedWorkoutLogMaster.objects.all()
    serializer_class = WeightedWorkoutLogMasterSerializer


class CardioWorkoutLogMasterViewSet(viewsets.ModelViewSet):
    """
    Viewset for viewing, creating, and Adding Cardio workout logs.
    """

    queryset = CardioWorkoutLogMaster.objects.all()
    serializer_class = CardioWorkoutLogMasterSerializer
