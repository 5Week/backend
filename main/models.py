from django.db import models

# Create your models here.

class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20,null=True)
    content = models.TextField()
    writer = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'
