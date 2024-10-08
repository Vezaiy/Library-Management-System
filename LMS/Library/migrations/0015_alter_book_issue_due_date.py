import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_alter_book_issue_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 20, 31, 15, 598860), help_text='Date the book is due to'),
        ),
    ]
