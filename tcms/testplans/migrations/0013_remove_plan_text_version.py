# Generated by Django 2.0.6 on 2018-06-26 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testplans', '0012_increase_checksum_field_size'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testplantext',
            options={'ordering': ['plan', '-pk']},
        ),
        migrations.AlterUniqueTogether(
            name='testplantext',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='testplantext',
            name='plan_text_version',
        ),
    ]
