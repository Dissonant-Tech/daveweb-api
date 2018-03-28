from django.db import models
from django.apps import apps
from django.conf import settings
from django.utils.text import Truncator

from markdownx.models import MarkdownxField


CARD_STYLE_CHOICES = (
    ('AR', 'Article'),  # Links to an article. Uses title from article
    ('BA', 'Banner'),   # Text body is central. Uses title
    ('QU', 'Quote'),    # Used for quotes. Has footer. No title
    ('IM', 'Image'),    # Image in top part of card
)


class Category(models.Model):
    """Category Model"""
    title = models.CharField(
        max_length=100,
        db_index=True,
        unique=True,
        verbose_name='Title',
    )
    slug = models.SlugField(
        max_length=100,
        db_index=True,
    )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'


class Article(models.Model):
    """Article Model"""
    title = models.CharField(
        max_length=100,
        null=True,
        verbose_name='Title'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Slug',
        help_text='Uri Identifier',
        blank=True,
        max_length=255
    )
    content = MarkdownxField()
    created_at = models.DateField(
        db_index=True,
        verbose_name='Date Created'
    )
    published = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name='Published',
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name='Categories',
        blank=True
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='User'
    )

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created_at']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Card(models.Model):
    """Card Model
    Abstract class to hold card information shared by all types of cards"""
    DEFAULT_STYLE = 'BA'

    text = models.TextField(
        null=False,
        blank=False,
        verbose_name='text',
    )
    created_at = models.DateField(
        db_index=True,
        auto_now_add=True,
        verbose_name='Created at'
    )
    date_visible = models.BooleanField(
        default=False,
        verbose_name='Date is Visible'
    )
    classes = models.CharField(
        max_length=200,
        null=True
    )
    style = models.CharField(
        max_length=2,
        choices=CARD_STYLE_CHOICES,
        default=DEFAULT_STYLE
    )

    def __init__(self, *args, **kwargs):
        super(Card, self).__init__(*args, **kwargs)
        if not self.pk and not self.style:
            self.style = self.DEFAULT_STYLE

    def __str__(self):
        return 'Card: %s' % self.id

    class Meta:
        abstract=True
        ordering = ['-created_at']


class ArticleCard(Card):
    """ArticleCard Model"""
    DEFAULT_STYLE = 'AR'

    article = models.ForeignKey(
        Article,
        verbose_name='Article',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        null=False,
        verbose_name='text',
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.text:
            self.text = Article.objects.get(pk=self.article.id).content
            self.text = Truncator(self.text).words(apps.get_app_config('blog')
                                                   .CARD_TRUNCATE_SIZE)

        super(ArticleCard, self).save(*args, **kwargs)


class BannerCard(Card):
    DEFAULT_STYLE = 'BA'

    title = models.CharField(
        max_length=120,
        verbose_name='Title'
    )


class QuoteCard(Card):
    """QuoteCard Model"""
    DEFAULT_STYLE = 'QU'

    footer = models.CharField(
        max_length=120,
        verbose_name='Footer'
    )


class ImageCard(Card):
    DEFAULT_STYLE = 'IM'

    image = models.ImageField(
        upload_to='card-images/%Y/'
    )
