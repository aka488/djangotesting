from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

# Create your models here.

class User(BaseModel):
	userkey = db.StringListProperty(default=[])
	displayname = db.StringProperty(default=[])
	type = db.StrinogProperty(choices=("admin", "member"),default ="member")

	#contact information
	email = db.StringProperty(default="")
	phone = db.StringProperty(default="")
	phone_mobile = db.StringProperty(default="")
	


