from django.contrib import admin

from tasks.models import Skill, Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "creation_date",
        "start_date",
        "end_date",
        "status",
        "display_skills",
    )

    def display_skills(self, obj):
        return ", ".join([skill.skill_name for skill in obj.skill.all()])


class SkillAdmin(admin.ModelAdmin):
    list_display = ["skill_name"]


admin.site.register(Skill, SkillAdmin)
admin.site.register(Task, TaskAdmin)
