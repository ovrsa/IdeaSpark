from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)


# 1対多
class Comment(models.Model):
    # on_deleteでは、親モデルが削除されたときに、子モデルのレコードも一緒に削除される
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # EmailFieldがjangoにはある
    email = models.EmailField()
    body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)

