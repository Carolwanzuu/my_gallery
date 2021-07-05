# Generated by Django 3.2.5 on 2021-07-05 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20210705_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photos.category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_description',
            field=models.TextField(blank=True),
        ),
    ]