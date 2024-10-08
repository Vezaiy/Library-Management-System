import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_alter_book_issue_return_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_issue',
            old_name='borrowed',
            new_name='Is_borrowed',
        ),
        migrations.RemoveField(
            model_name='book_issue',
            name='returned',
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 15, 12, 23, 54, 414185)),
        ),
    ]
