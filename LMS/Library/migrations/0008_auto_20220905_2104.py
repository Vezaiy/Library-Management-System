import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20220904_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 21, 4, 34, 312252)),
        ),
        migrations.AlterField(
            model_name='students',
            name='roll_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
