# Generated by Django 4.1 on 2022-08-05 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
