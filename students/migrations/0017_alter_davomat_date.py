# Generated by Django 4.1.4 on 2023-02-15 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_alter_davomat_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='davomat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 15, 15, 42, 45, 437329)),
        ),
    ]
