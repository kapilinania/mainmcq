# Generated by Django 4.2.4 on 2023-08-11 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.GenericIPAddressField()),
                ('mac_address', models.CharField(max_length=17)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cpu_count', models.CharField(max_length=50)),
                ('total_memory', models.BigIntegerField(default=10019)),
                ('available_memory', models.BigIntegerField(default=10012)),
                ('used_memory', models.BigIntegerField(default=10018)),
                ('free_memory', models.BigIntegerField(default=10015)),
                ('bytes_sent', models.BigIntegerField(default=10014)),
                ('bytes_received', models.BigIntegerField(default=10013)),
                ('packets_sent', models.BigIntegerField(default=100017)),
                ('packets_received', models.BigIntegerField(default=10016)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_text', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalmcq.question')),
            ],
        ),
    ]