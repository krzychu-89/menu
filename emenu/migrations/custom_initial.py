from django.db import migrations, connection

# you can add more sql files here later on, bc these are just for testing
def run_raw_sql(apps, schema_editor):
    f = open('./emenu/sql/create_schema.sql', 'r')
    sql = f.read()
    with connection.cursor() as cursor:
        cursor.execute(sql)

def reverse_run_raw_sql(apps, schema_editor):
    pass  # fake

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(run_raw_sql, reverse_run_raw_sql),
        ]