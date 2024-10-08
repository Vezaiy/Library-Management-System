import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20220907_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_issue',
            name='Is_borrowed',
        ),
        migrations.RemoveField(
            model_name='book_issue',
            name='book',
        ),
        migrations.RemoveField(
            model_name='book_issue',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='book_issue',
            name='return_date',
        ),
        migrations.AddField(
            model_name='book_issue',
            name='date_returned',
            field=models.DateField(blank=True, help_text='Date the book is returned', null=True),
        ),
        migrations.AddField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 17, 8, 45, 905171), help_text='Date the book is due to'),
        ),
        migrations.AddField(
            model_name='book_issue',
            name='remarks_on_issue',
            field=models.CharField(default='Some Remarks', help_text='Book remarks/condition during issue', max_length=100),
        ),
        migrations.AddField(
            model_name='book_issue',
            name='remarks_on_return',
            field=models.CharField(default='Some Remarks', help_text='Book remarks/condition during return', max_length=100),
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='issue_date',
            field=models.DateTimeField(auto_now=True, help_text='Date the book is issued'),
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Book unique id across the Library', primary_key=True, serialize=False)),
                ('Is_borrowed', models.BooleanField(default=False)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
        migrations.AddField(
            model_name='book_issue',
            name='book_instance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.bookinstance'),
            preserve_default=False,
        ),
    ]
