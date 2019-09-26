from django.db import models


class Content (models.Model):
    """やる内容のモデル
    """
    content_name = models.CharField(max_length=200)
    content_desc = models.CharField(max_length=400)

    def __str__(self):
        return self.content_name


class Ticket (models.Model):
    """やることリストのチケットのモデル
    """
    ticket_id = models.CharField(max_length=20)
    ticket_name = models.CharField(max_length=50)
    created_date = models.DateField('date created')
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.ticket_name
