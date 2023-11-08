from rest_framework import serializers

from .models import (
    WorkoutMaster,
    ProgramMaster,
    WeightedWorkoutLogMaster,
    CardioWorkoutLogMaster,
)

# Create your serializers here.


class WorkoutMasterSerializer(serializers.ModelSerializer):
    """
    Serializer for storing workouts.
    """

    class Meta:
        model = WorkoutMaster
        fields = ["id", "name", "workout_type"]


class ProgramMasterSerializer(serializers.ModelSerializer):
    """
    Serializer for storing workouts.
    """

    workouts = serializers.SlugRelatedField(
        many=True, queryset=WorkoutMaster.objects.all(), slug_field="name"
    )

    class Meta:
        model = ProgramMaster
        fields = ["id", "name", "workouts", "start_date", "end_date"]


class WeightedWorkoutLogMasterSerializer(serializers.ModelSerializer):
    workout = serializers.SlugRelatedField(
        slug_field="name", queryset=WorkoutMaster.objects.all()
    )

    class Meta:
        model = WeightedWorkoutLogMaster
        fields = [
            "id",
            "workout",
            "date_time",
            "sets",
            "repetition",
            "weight",
            "weight_metric",
            "calories",
        ]


class CardioWorkoutLogMasterSerializer(serializers.ModelSerializer):
    workout = serializers.SlugRelatedField(
        queryset=WorkoutMaster.objects.all(), slug_field="name"
    )

    class Meta:
        model = CardioWorkoutLogMaster
        fields = [
            "id",
            "workout",
            "laps",
            "distance",
            "date_time",
            "calories",
        ]
