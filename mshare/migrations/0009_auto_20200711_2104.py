# Generated by Django 3.0.7 on 2020-07-11 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mshare', '0008_auto_20200711_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='current_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='currentitem', to='mshare.Share'),
        ),
    ]
