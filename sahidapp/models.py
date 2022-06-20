from email.mime import image
from statistics import mode
from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

# Create your models here.

class SiteIdentity(models.Model):
    site_name = models.CharField(max_length=500, null=True, blank=True)
    tagline = models.CharField(max_length=3000, blank=True, null=True)
    logo_first = models.ImageField(blank=True, null=True, upload_to="static/images")
    logo_second = models.ImageField(blank=True, null=True, upload_to="static/images")
    favicon = models.ImageField(blank=True, null=True, upload_to="static/images")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'logo'

    def __str__(self):
        return str(self.site_name)

class Menu(models.Model):
    menu_name = models.CharField(max_length=300, null=True, blank=True)
    menu_link = models.URLField(max_length=500, null=True, blank=True)
    menu_position = models.CharField(max_length=200, null=True, blank=True)
    menu_type = models.CharField(max_length=200, null=True, blank=True)
    menu_index = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="static/images")
    short_content = RichTextField(null=True, blank=True)
    long_content = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'menu'

    def __str__(self):
        return str(self.menu_name)


class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    sub_menu_name = models.CharField(max_length=300, null=True, blank=True)
    link_name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="static/images")
    short_content = RichTextField(null=True, blank=True)
    long_content = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sub Menu'

    def __str__(self):
        return str(self.sub_menu_name)
 

class Banner(models.Model):
    banner_image = models.ImageField(
        blank=True, null=True, upload_to="static/banner")
    banner_text = models.CharField(max_length=1000, blank=True, null=True)
    banner_link = models.URLField(max_length=500, null=True, blank=True)
    button_text = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Banner'

    def __str__(self):
        return str(self.banner_text)

class Service(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="static/images")
    title = models.CharField(max_length=300, null=True, blank=True)
    short_desc = RichTextField(blank=True, null=True)
    long_desc = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Service'

    def __str__(self):
        return str(self.title)

class Destination(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="static/images")
    title = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'destination'

    def __str__(self):
        return str(self.title)

class JobCategory(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="static/images")
    short_desc = RichTextField(blank=True, null=True)
    long_desc = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'JobCategory'

    def __str__(self):
        return str(self.title)

class JobListing(models.Model):
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to="static/images")
    company_name = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    short_desc = RichTextField(blank=True, null=True)
    long_desc = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'JobListing'

    def __str__(self):
        return str(self.title)

class Client(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="static/images")
    title = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'client'

    def __str__(self):
        return str(self.title)

class Contact(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    message = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return str(self.name)

class AboutSection(models.Model):
    about_image = models.ImageField(
        blank=True, null=True, upload_to="static/images")
    image_two = models.ImageField(
        blank=True, null=True, upload_to="static/images")
    image_three = models.ImageField(
        blank=True, null=True, upload_to="static/images")
    short_desc = RichTextField(blank=True, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    tagline = models.CharField(max_length=200, null=True, blank=True)
    long_desc = RichTextField(blank=True, null=True)
    about_link = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'About'

    def __str__(self):
        return str(self.about_link)


# Job category.........
class News(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    tagline = models.CharField(max_length=300, blank=True, null=True)
    heading = models.CharField(max_length=500, blank=True, null=True)
    news_image = models.ImageField(
        blank=True, null=True, upload_to="static/news")
    short_desc = RichTextField(null=True, blank=True)
    long_desc = RichTextField(null=True, blank=True)
    news_link = models.CharField(max_length=300, blank=True, null=True)
    news_position = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'News'

    def __str__(self):
        return str(self.title)


class Message(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="static/images")
    name = models.CharField(max_length=1000, null=True, blank=True)
    position = models.CharField(max_length=500, null=True, blank=True)
    short_desc = RichTextField(blank=True, null=True)
    long_desc = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Message'

    def __str__(self):
        return str(self.name)


class Gallery(models.Model):
    media = models.FileField(blank=True, null=True, upload_to="static/gallery")
    media_type = models.CharField(max_length=300, null=True, blank=True)
    video_url = models.URLField(max_length=3000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Gallery'

    def __str__(self):
        return str(self.media_type)

class Blog(models.Model):
    blog_image = models.ImageField(blank=True, null=True, upload_to="static/blogs")
    blog_title = models.CharField(max_length=500, blank=True, null=True)
    blog_author = models.CharField(max_length=500, blank=True, null=True)
    short_desc = RichTextField(blank=True, null=True)
    long_desc = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Blog'

    def __str__(self):
        return str(self.blog_title)

class Testimonial(models.Model):
    student_image = models.ImageField(
        blank=True, null=True, upload_to="static/testimonial")
    student_name = models.CharField(max_length=500, null=True, blank=True)
    short_message = RichTextField(null=True, blank=True)
    long_message = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Testimonial'

    def __str__(self):
        return str(self.student_name)


class Footer(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=300, blank=True, null=True)
    instagram = models.URLField(max_length=300, blank=True, null=True)
    twitter = models.URLField(max_length=300, blank=True, null=True)
    youtube = models.URLField(max_length=300, blank=True, null=True)
    tiktok = models.URLField(max_length=300, blank=True, null=True)
    license_no = models.CharField(max_length=200, blank=True, null=True)
    copyright = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Footer'

    def __str__(self):
        return str(self.email)

class Popup(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to="static/images")
    message = RichTextField(null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'popup'

    def __str__(self):
        return str(self.title)

class AdmissionForm(models.Model):
    full_name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    date_of_birth = models.CharField(max_length=500, null=True, blank=True)
    gender = models.CharField(max_length=500, null=True, blank=True)
    mobile_no = models.CharField(max_length=500, null=True, blank=True)
    current_address = models.CharField(max_length=500, null=True, blank=True)
    parent_name = models.CharField(max_length=500, null=True, blank=True)
    parent_no = models.CharField(max_length=500, null=True, blank=True)
    parent_email = models.EmailField(max_length=500, null=True, blank=True)
    gpa = models.CharField(max_length=500, null=True, blank=True)
    school_name = models.CharField(max_length=500, null=True, blank=True)
    school_address = models.CharField(max_length=500, null=True, blank=True)
    stream = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'admissionform'

    def __str__(self):
        return str(self.full_name)

class Counter(models.Model):
    value = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="static/images")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'counter'

    def __str__(self):
        return str(self.name)

class SelectionProcess(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="static/images")
    long_desc = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'selectionprocess'

    def __str__(self):
        return str(self.title)