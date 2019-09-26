from django.db import models


class Content (models.Model):
    """やる内容のモデル
    """
    content_name = models.CharField(max_length=200)
    content_desc = models.CharField(max_length=400)


class Ticket (models.Model):
    """やることリストのチケットのモデル
    """
    ticket_id = models.CharField(max_length=20)
    created_date = models.DateField('date created')
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
