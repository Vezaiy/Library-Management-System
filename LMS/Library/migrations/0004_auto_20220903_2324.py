

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20220903_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_pages',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 23, 24, 3, 991491)),
        ),
    ]
