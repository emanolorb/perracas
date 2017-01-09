from django.db import models
import os


class HomePageImage(models.Model):
    favicon = models.ImageField()
    main_icon = models.ImageField()
    parallax_image1 = models.ImageField()
    parallax_image2 = models.ImageField()

    def save(self, *args, **kwargs):
        data = HomePageImage.objects.filter()
        if data:
            for obj in data:
                favicon_var = '%s' %(obj.favicon.name)
                faviconurl = '%s' %(obj.favicon.path)
                main_icon_var = '%s' %(obj.main_icon.name)
                main_iconurl = '%s' %(obj.main_icon.path)
                parallax_image1_var = '%s' %(obj.parallax_image1.name)
                parallax_image1url = '%s' %(obj.parallax_image1.path)
                parallax_image2_var = '%s' %(obj.parallax_image2.name)
                parallax_image2url = '%s' %(obj.parallax_image2.path)
            if favicon_var != self.favicon.name:
                os.remove(faviconurl)
            if main_icon_var != self.main_icon.name:
                os.remove(main_iconurl)
            if parallax_image1_var != self.parallax_image1.name:
                os.remove(parallax_image1url)
            if parallax_image2_var != self.parallax_image2.name:
                os.remove(parallax_image2url)
        HomePageImage.objects.filter().delete()
        super(HomePageImage, self).save(*args, **kwargs)
        HomePageImage.objects.filter().update(id=1)

    def __str__(self):
        return '%s' % ('initial template')


class HomePageSlider(models.Model):
    slider_image = models.ImageField()
    big_tag_line = models.TextField()
    color_big_tag = models.CharField(
        max_length=10,
        choices=(('lighten-5', 'white'), ('darken-1', 'grey'), ('darken-4', 'black')))
    small_slogan = models.TextField()
    color_small_tag = models.CharField(
        max_length=10,
        choices=(('lighten-5', 'white'), ('darken-1', 'grey'), ('darken-4', 'black')))
    aligned_caption = models.CharField(
        max_length=10,
        choices=(('c', 'center'), ('l', 'left'), ('r', 'right')),)

    def __str__(self):
        return '%s - %s' % (self.id, self.big_tag_line)


class HomePageText(models.Model):
    title = models.CharField(max_length=80)
    color_title = models.CharField(
        max_length=10,
        choices=(('lighten-5', 'white'), ('darken-1', 'grey'), ('darken-4', 'black')))
    subtitle = models.TextField()
    color_small_tag = models.CharField(
        max_length=10,
        choices=(('lighten-5', 'white'), ('darken-1', 'grey'), ('darken-4', 'black')))
    blank_panel_title = models.CharField(max_length = 80)
    blank_panel_text = models.TextField()
    blank_panel_title2 = models.CharField(max_length = 80)
    blank_panel_text_2 = models.TextField()

    def save(self, *args, **kwargs):
        HomePageText.objects.filter().delete()
        super(HomePageText, self).save(*args, **kwargs)
        HomePageText.objects.filter().update(id=1)

    def __str__(self):
        return '%s - %s' % ('Initial text template', self.title)


class ContactPageImage(models.Model):
    contact_image = models.ImageField()
    text1 = models.TextField()
    text2 = models.TextField()

    def save(self, *args, **kwargs):
        data = ContactPageImage.objects.filter()
        if data:
            for obj in data:
                contact_imagepath = '%s' %(obj.contact_image.path)
                contact_imagename = '%s' %(obj.contact_image.name)
            if contact_imagename != self.contact_image.name:
                os.remove(contact_imagepath)
        ContactPageImage.objects.filter().delete()
        super(ContactPageImage, self).save(*args, **kwargs)
        ContactPageImage.objects.filter().update(id=1)

    def __str__(self):
        return '%s - %s' % ('Initial imge contact-template', self.contact_image)
