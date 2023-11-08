from django.urls import path, include
from rest_framework.routers import DefaultRouter
from workout import views

# define your routers here.
router = DefaultRouter()

router.register(r"workouts", views.WorkoutMasterViewSet, basename="workout")
router.register(r"programs", views.ProgramMasterViewSet, basename="program")
router.register(
    r"weighted-workout-logs",
    views.WeightedWorkoutLogMasterViewSet,
    basename="weighted-workout-logs",
)
router.register(
    r"cardio-workout-logs",
    views.CardioWorkoutLogMasterViewSet,
    basename="cardio-workout-logs",
)

urlpatterns = [
    path("", include(router.urls)),
]
