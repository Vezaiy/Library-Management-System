import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_alter_book_issue_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 9, 20, 53, 551953), help_text='Date the book is due to'),
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='remarks_on_issue',
            field=models.CharField(default='Book in good condition', help_text='Book remarks/condition during issue', max_length=100),
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='remarks_on_return',
            field=models.CharField(default='Book in good condition', help_text='Book remarks/condition during return', max_length=100),
        ),
    ]
