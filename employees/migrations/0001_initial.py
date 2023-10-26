# Generated by Django 4.2.6 on 2023-10-25 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('specialty', models.CharField(max_length=255)),
                ('protected_time', models.DateTimeField(auto_now_add=True)),
                ('academic_degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.academicdegree')),
                ('academic_rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.academicrank')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.position')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.rank')),
            ],
        ),
    ]
