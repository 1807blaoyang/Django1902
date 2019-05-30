# Generated by Django 2.2.1 on 2019-05-15 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='bdate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bttile',
            field=models.CharField(max_length=30, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.BookInfo', verbose_name='所属书籍'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='gender',
            field=models.CharField(choices=[(0, '男'), (1, '女')], max_length=10),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='name',
            field=models.CharField(max_length=30, verbose_name='英雄'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='skill',
            field=models.CharField(max_length=50, null=True, verbose_name='技能'),
        ),
    ]
