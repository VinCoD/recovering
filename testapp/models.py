from django.db import models

# Create your models here.
class Test(models.Model):
    """A test Table"""
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    comment = models.TextField(max_length=250)

    def __str__(self):
        return self.name

class New(models.Model):
    """Another test table"""
    author = models.ForeignKey(Test, on_delete=models.CASCADE)
    time_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=500, null=True)


    def __str__(self):
        return self.title

class Relative(models.Model):
    cousin = models.ManyToManyField(Test)
    meeting = models.CharField(max_length=20, null=True)
    details = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.meeting

class Remark(models.Model):
    subject = models.CharField(max_length=100, null=True)
    name = models.ForeignKey(Test, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)

    def __str__(self):
        return self.subject