# Generated by Django 3.0.7 on 2020-06-25 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsuite', '0004_auto_20200625_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResultDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_result_details', to='testsuite.Question')),
                ('test_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_result_details', to='testsuite.TestResult')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_result_details', to='testsuite.Variant')),
            ],
        ),
        migrations.DeleteModel(
            name='TestRunDetail',
        ),
    ]