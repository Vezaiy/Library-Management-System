import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20220908_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='book_number',
            field=models.PositiveIntegerField(help_text='Book number', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_pages',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 20, 11, 6, 390132), help_text='Date the book is due to'),
        ),
    ]
