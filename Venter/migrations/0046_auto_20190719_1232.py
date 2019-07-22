# Generated by Django 2.1.2 on 2019-07-19 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Venter', '0045_auto_20190719_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='domain_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='domain',
            unique_together={('proposal_name', 'domain_name')},
        ),
    ]