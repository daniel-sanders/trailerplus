# Generated by Django 3.0.8 on 2020-08-07 14:24

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Facebook link', null=True)),
                ('instagram', models.URLField(blank=True, help_text='Instagram link', null=True)),
                ('youtube', models.URLField(blank=True, help_text='Youtube link', null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ErrorPage404',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', wagtail.core.fields.StreamField([('slider_block', wagtail.core.blocks.StructBlock([('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='To highlight the word into red please put it inside these tags: <b>…text…</b>', max_length=999, required=False))])))])), ('big_text_section_block', wagtail.core.blocks.StructBlock([('text_block_top', wagtail.core.blocks.TextBlock(required=False)), ('text_block_top_subtext', wagtail.core.blocks.TextBlock(max_length=999, required=False))])), ('category_carousel', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('category_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='To highlight the word into red please put it inside these tags: <b>…text…</b>', required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=55, required=True)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('social_icons_banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Join The TrailersPlus Community', required=False)), ('text', wagtail.core.blocks.CharBlock(default='Stay Up to Date With the Latest and Greatest', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('partners', streams.blocks.PartnersBlock()), ('banners_block', wagtail.core.blocks.StructBlock([('title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_left_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_left', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('left_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500)), ('title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_right_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_right', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('right_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500))])), ('recent_works', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, max_length=250)), ('background_color_grey', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('works', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_title', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))])))])), ('trustpilot_widget', streams.blocks.TrustPilotWidget())], blank=True, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
