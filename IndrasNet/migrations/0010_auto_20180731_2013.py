# Generated by Django 2.0.6 on 2018-07-31 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndrasNet', '0009_auto_20180731_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='plot_type',
            field=models.CharField(choices=[('NO', 'None'), ('SC', 'Scatterplot'), ('LN', 'Line')], default=None, max_length=2, null=True),
        ),
    ]
