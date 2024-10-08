

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_issue_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_pages',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 23, 23, 1, 769824)),
        ),
    ]
