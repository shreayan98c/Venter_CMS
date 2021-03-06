# Generated by Django 2.1.2 on 2019-06-25 09:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Venter', '0036_auto_20190625_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='proposal_name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Proposal name cannot contain special characters: @_!#$%^&*()<>?/\\|}{~:', regex='^[@_!#$%^&*()<>?/\\|}{~:]$')]),
        ),
    ]
