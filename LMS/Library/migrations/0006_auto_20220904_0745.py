import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_book_issue_return_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='std_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='std_name',
            new_name='fullname',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='std_rn',
            new_name='program',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='std_study_pro',
            new_name='roll_number',
        ),
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, help_text='Summary about the book', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='book_issue',
            name='borrowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book_issue',
            name='returned',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='students',
            name='Guardian_name',
            field=models.CharField(default='Guardian name', help_text='parent/guardian full name', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 7, 44, 40, 874707)),
        ),
    ]
