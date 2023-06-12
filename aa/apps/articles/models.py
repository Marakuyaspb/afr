import datetime
from django.db import models
# from django db.utils import timezone

class Article(models.Model):
	art_title = models.CharField('article name', max_length = 200)
	art_text = models.TextField('article text')
	art_pub_date = models.DateTimeField('publication date')
	art_picture = models.FileField('picture')

	def __str__(self):
		return self.art_title

	def was_published_recently(self):
		return self.art_pub_date >= (timezone.now() - dstetime.timedelta(days = 7))

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('author name', max_length = 70)
	comment_text = models.CharField('comment text', max_length = 500)

	def __str__(self):
		return self.author_name