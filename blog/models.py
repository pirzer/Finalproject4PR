from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import timedelta
from django.utils import timezone
# timedelta, timezone were added


# TO BE updated STATUS below
# STATUS = ((0, "Draft"), (1, "Scheduled"), (2, "Cancelled"))
# AUDIENCE = ((0, "Admin"), (1, "Everyone"))

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
# Create your models here.
# Classed added Event, Meta below


class Event(models.Model):
    '''This class defines the Event model'''
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_events"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    text_preview = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    joins = models.ManyToManyField(
        User, related_name='blogevent_like', blank=True)
    # The next field sets the date +14 days at the time of creation
    # to give enough time to admins to approve and organize the event
    # if JS is disabled on front-end, the date+14 automatically pre-populates
    # the field in the form
    scheduled_on = models.DateTimeField(default=timezone.now() +
                                        timedelta(days=14))

    class Meta:
        '''The following line defines the ascending order that data is
           retrieved by, based on the field scheduled_on:
           the closer the date, the higher in the page'''
        ordering = ["scheduled_on"]

    def __str__(self):
        '''Returns the title field of the created instance'''
        return self.title

    def number_of_joins(self):
        '''Returns the number of entries/values within the field joins'''
        return self.joins.count()
