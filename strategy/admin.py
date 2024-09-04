from django.contrib import admin
from .models import StrategicObjective, KeyActivity, ProgressReport

# Register the StrategicObjective model
@admin.register(StrategicObjective)
class StrategicObjectiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

# Register the KeyActivity model
@admin.register(KeyActivity)
class KeyActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_name', 'objective', 'expected_output', 'budget', 'responsibility')
    search_fields = ('activity_name', 'objective__title')
    list_filter = ('objective', 'responsibility')

# Register the ProgressReport model
@admin.register(ProgressReport)
class ProgressReportAdmin(admin.ModelAdmin):
    list_display = ('activity', 'report_date', 'status')
    search_fields = ('activity__activity_name',)
    list_filter = ('status', 'report_date')
