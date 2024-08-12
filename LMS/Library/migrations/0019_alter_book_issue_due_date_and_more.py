
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_auto_20220910_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 6, 0, 17, 8, 510964), help_text='Date the book is due to'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='book_number',
            field=models.PositiveIntegerField(help_text='Book number for books of the save kind', null=True),
        ),
    ]
