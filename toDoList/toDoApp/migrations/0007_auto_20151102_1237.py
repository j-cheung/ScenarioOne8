# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoApp', '0006_list_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='theList',
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
