# Generated by Django 3.2.4 on 2021-06-17 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingTypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reading_type', models.TextField()),
            ],
            options={
                'db_table': 'reading_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('read_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='htc.readingtypes')),
            ],
            options={
                'db_table': 'reading',
                'managed': True,
            },
        ),
    ]