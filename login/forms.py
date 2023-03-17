from django.forms import ModelForm
from .models import Post
from home.models import Documents

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'text']

class DocumentForm(ModelForm):
    class Meta:
        model = Documents
        fields = ['title', 'pdf', 'description']
