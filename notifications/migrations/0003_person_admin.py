# Generated by Django 2.2.1 on 2019-05-02 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20190502_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='underlings', to='notifications.Person'),
        ),
    ]
