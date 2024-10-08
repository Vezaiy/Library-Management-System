import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('book_author', models.CharField(max_length=100)),
                ('book_pages', models.IntegerField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_rn', models.CharField(max_length=100)),
                ('std_name', models.CharField(max_length=100)),
                ('std_address', models.CharField(max_length=100)),
                ('std_study_pro', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(auto_now=True)),
                ('return_date', models.DateTimeField(default=datetime.datetime(2021, 10, 27, 9, 44, 34, 986902))),
                ('remarks', models.CharField(default='Some Remarks', max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.students')),
            ],
        ),
    ]
