from django.db import migrations


def create_customtext(apps, schema_editor):
    CustomText = apps.get_model("home", "CustomText")
    customtext_title = "PLAT-4990-Testing"

    CustomText.objects.create(title=customtext_title)


def create_homepage(apps, schema_editor):
    HomePage = apps.get_model("home", "HomePage")
    homepage_body = """
        <h1 class="display-4 text-center">PLAT-4990-Testing</h1>
        <p class="lead">
            This is the sample application created and deployed from the Crowdbotics app.
            You can view list of packages selected for this application below.
        </p>"""

    HomePage.objects.create(body=homepage_body)


def create_site(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    custom_domain = "plat-4990-testing-d-15520.botics.co"

    site_params = {
        "name": "PLAT-4990-Testing",
    }
    if custom_domain:
        site_params["domain"] = custom_domain

    Site.objects.update_or_create(defaults=site_params, id=1)


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RunPython(create_customtext),
        migrations.RunPython(create_homepage),
        migrations.RunPython(create_site),
    ]
