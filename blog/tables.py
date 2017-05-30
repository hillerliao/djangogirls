# tutorial/tables.py
import django_tables2 as tables
from .models import Post, Secs

class PostTable(tables.Table):
    class Meta:
        model = Post
        fields = ('id','title','text','published_date')
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class SecsTable(tables.Table):
    class Meta:
        model = Secs
        fields = ('sec_name','gqj_data','gqj_rank')
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}