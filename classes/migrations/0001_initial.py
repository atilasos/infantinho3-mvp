# Generated by Django 5.2 on 2025-04-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the class, e.g., "5º A", "Turma Azul".', max_length=100, verbose_name='class name')),
                ('year', models.IntegerField(help_text='Starting year of the academic year (e.g., 2024 for 2024/2025) or the grade level (e.g., 5 for 5th grade).', verbose_name='academic year')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
                'ordering': ['year', 'name'],
            },
        ),
    ]
