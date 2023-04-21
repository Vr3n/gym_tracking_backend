from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.


class WorkoutMaster(models.Model):
    """
    The workouts which gym member will perform.
    """

    WORKOUT_TYPES = (
        ("WEIGHT LIFTING", "WEIGHTS"),
        ("CARDIO", "CARDIO"),
    )

    name = models.CharField(_("Workout Name"), max_length=256)
    workout_type = models.CharField(
        _("Workout Type"), max_length=256, choices=WORKOUT_TYPES, default="WEIGHTS"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProgramMaster(models.Model):
    """
    Details of the Program alloted to User.
    """

    name = models.CharField(_("Program Name"), max_length=256)
    workouts = models.ManyToManyField(WorkoutMaster, related_name="workouts")
    start_date = models.DateField(_("Program Start Date"), default=datetime.now)
    end_date = models.DateField(_("Program End Date"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class ProgramLogMaster(models.Model):
    """
    Logging when you worked out the Program.
    """

    program = models.ForeignKey(ProgramMaster, on_delete=models.CASCADE)
    date_time = models.DateTimeField(_("Program Date"), default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.program.name} on {self.date_time.strftime('%m/%d/%Y, %H:%M:%S')}"


class WeightedWorkoutLogMaster(models.Model):
    """
    Logging the Workouts with their details.
    Weighted Workouts.
    """

    WEIGHT_METRIC = (
        ("Kilo Grams", "KG"),
        ("Pounds", "LBS"),
    )

    workout = models.ForeignKey(WorkoutMaster, on_delete=models.CASCADE)
    date_time = models.DateTimeField(_("Workout Date"), default=datetime.now)
    sets = models.PositiveIntegerField(_("Workout Sets"))
    repetition = models.PositiveIntegerField(_("Workout Repetitions"))
    weight = models.PositiveIntegerField(_("Weight Lifted"), blank=True, null=True)
    weight_metric = models.CharField(
        _("Weight Metric"), max_length=256, choices=WEIGHT_METRIC, blank=True, null=True
    )
    calories = models.CharField(
        _("Calories Burned"), max_length=256, blank=True, null=True
    )
