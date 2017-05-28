# tutorial/tables.py
import django_tables2 as tables
from .models import Post

class PostTable(tables.Table):
    class Meta:
        model = Post
        fields = ('id','title','text','published_date')
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}