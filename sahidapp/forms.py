from django.forms import ModelForm
from .models import *


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

class SubMenuForm(ModelForm):
    class Meta:
        model = SubMenu
        fields = '__all__'

class AboutForm(ModelForm):
    class Meta:
        model = AboutSection
        fields = '__all__'

class ServicesForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class JobCategoryForm(ModelForm):
    class Meta:
        model = JobCategory
        fields = '__all__'

class JobForm(ModelForm):
    class Meta:
        model = JobListing
        fields = '__all__'

class BlogsForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'

class TeamsForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

class FooterForm(ModelForm):
    class Meta:
        model = Footer
        fields = '__all__'

class PopupForm(ModelForm):
    class Meta:
        model = Popup
        fields = '__all__'