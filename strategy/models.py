from django.db import models

# Create your models here.
class StrategicObjective(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class KeyActivity(models.Model):
    objective = models.ForeignKey(StrategicObjective, on_delete=models.CASCADE, related_name='activities')
    activity_name = models.CharField(max_length=255)
    expected_output = models.CharField(max_length=255)
    output_indicators = models.CharField(max_length=255)
    year1_target = models.IntegerField()
    year2_target = models.IntegerField()
    year3_target = models.IntegerField()
    year4_target = models.IntegerField()
    year5_target = models.IntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    responsibility = models.CharField(max_length=255)
    support = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.activity_name

class ProgressReport(models.Model):
    activity = models.ForeignKey(KeyActivity, on_delete=models.CASCADE, related_name='progress_reports')
    report_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('On Track', 'On Track'), ('At Risk', 'At Risk'), ('Completed', 'Completed')])
    comments = models.TextField()

    def __str__(self):
        return f'{self.activity.activity_name} - {self.report_date}'
