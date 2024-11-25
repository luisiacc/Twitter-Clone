# Generated by Django 5.0.6 on 2024-10-17 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_customuser_name_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='follows',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]