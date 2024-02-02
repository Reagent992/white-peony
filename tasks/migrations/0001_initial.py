# Generated by Django 5.0.1 on 2024-01-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "skill_name",
                    models.CharField(max_length=255, verbose_name="Навык"),
                ),
            ],
            options={
                "verbose_name": "Навыки",
                "verbose_name_plural": "Навыки",
                "ordering": ("skill_name",),
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=150, verbose_name="Название задачи"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Описание задачи",
                    ),
                ),
                (
                    "creation_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Дата создания задачи"
                    ),
                ),
                (
                    "start_date",
                    models.DateField(
                        verbose_name="Дата начала работ по задаче"
                    ),
                ),
                ("end_date", models.DateField(verbose_name="Дедлайн задачи")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("complete", "Выполнен"),
                            ("in_progress", "В работе"),
                            ("cancel", "Отменен"),
                            ("trail", "Отстает"),
                        ],
                        default="in_progress",
                        max_length=20,
                        verbose_name="Статус задачи",
                    ),
                ),
            ],
            options={
                "verbose_name": "Задачи",
                "verbose_name_plural": "Задачи",
                "ordering": ("-creator",),
            },
        ),
    ]
