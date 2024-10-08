import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20220904_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='Email',
            field=models.EmailField(default='none@gmail.com', help_text='Guardian/parent e-mail', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 15, 30, 2, 352794)),
        ),
    ]
