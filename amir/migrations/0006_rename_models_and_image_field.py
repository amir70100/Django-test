from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amir', '0005_post_author'),
    ]

    operations = [
        migrations.RenameField('post', 'imaje', 'image'),
    ]
