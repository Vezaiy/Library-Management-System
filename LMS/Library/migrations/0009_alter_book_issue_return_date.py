import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20220905_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 21, 35, 1, 529061)),
        ),
    ]
