from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    photo_url = models.TextField()
    # return str because you need to be able to select user from drop down

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    article = models.TextField()
    image_url = models.TextField()
    tags = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    # return str because you need to be able to select post from drop down

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=240)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content


class Clap(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='claps')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='claps')
