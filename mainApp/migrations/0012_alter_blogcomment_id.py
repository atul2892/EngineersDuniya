# Generated by Django 5.0.1 on 2024-03-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0011_alter_blogcomment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
