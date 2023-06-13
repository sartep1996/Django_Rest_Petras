from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator



# Create your models here.

class Band(models.Model):
    name = models.CharField(_("name"), max_length=50)

    class Meta:
        verbose_name = _("band")
        verbose_name_plural = _("bands")

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("song_detail", kwargs={"pk": self.pk})
    

class Song(models.Model):
    title = models.CharField(_("title"), max_length=50)
    duration_validator = RegexValidator( regex=r'^\d{2}:\d{2}$', 
    message="Duration must be in the format 'MM:SS'."
    )
    duration = models.CharField(_('duration'), max_length=5, validators=[duration_validator])
    band = models.ForeignKey(
        Band, 
        verbose_name=_("band"), 
        on_delete=models.CASCADE,
        related_name = 'songs'
    )

    class Meta:
        verbose_name = _("song")
        verbose_name_plural = _("songs")

    def __str__(self):
        return f"{self.title} {self.duration} {self.band}"

    def get_absolute_url(self):
        return reverse("song_detail", kwargs={"pk": self.pk})
    

class SongReview(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name = 'reviews'
    )
    song = models.ForeignKey(
        Song, 
        verbose_name=_("song"), 
        on_delete=models.CASCADE,
        related_name= 'reviews'
    )
    content = models.TextField(_("content"), max_length=10000)
    # score = models.IntegerField(_('score'), max_length=2)\
    
    SCORE = (
        (1, '1/10'),
        (2, '2/10'),
        (3, '3/10'),
        (4, '4/10'),
        (5, '5/10'),
        (6, '6/10'),
        (7, '7/10'),
        (8, '8/10'),
        (9, '9/10'),
        (10, '10/10')
    )

    score = models.PositiveSmallIntegerField(_("score"), default=1, choices=SCORE)
    
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name = _("song review")
        verbose_name_plural = _("song reviews")

    def __str__(self):
        return f"{self.user} {self.song} {self.score} {self.created_at}"

    def get_absolute_url(self):
        return reverse("songreview_detail", kwargs={"pk": self.pk})

class SongReviewComment(models.Model):  
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name = 'comments'
    )
    song_review = models.ForeignKey(
        SongReview, 
        verbose_name=_("song review"), 
        on_delete=models.CASCADE,
        related_name= 'review_comments'
    )
    content = models.TextField(_("content"), max_length=10000)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name = _("song review comment")
        verbose_name_plural = _("song review comments")

    def __str__(self):
        return f"{self.user} {self.song_review}"

    def get_absolute_url(self):
        return reverse("songreviewcomment_detail", kwargs={"pk": self.pk})
    


class SongReviewLike(models.Model):
    user = models.ForeignKey(
    User, 
    verbose_name=_("user"), 
    on_delete=models.CASCADE,
    related_name = 'likes'
)
    song_review = models.ForeignKey(
    SongReview, 
    verbose_name=_("song review"), 
    on_delete=models.CASCADE,
    related_name= 'review_likes'
)

    class Meta:
        verbose_name = _("song review like")
        verbose_name_plural = _("song review like")

    def __str__(self):
        return f"{self.user} {self.song_review} {self.created_at}"

    def get_absolute_url(self):
        return reverse("songreviewlike_detail", kwargs={"pk": self.pk})



    
    
