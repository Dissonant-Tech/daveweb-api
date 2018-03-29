from django.db import models
from django.apps import apps
from django.conf import settings
from django.utils.text import Truncator, slugify

from markdownx.models import MarkdownxField


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
        blank=True,
    )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

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

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created_at']


class Card(models.Model):
    """Card Model
    Abstract class to hold card information shared by all types of cards"""

    text = models.TextField(
        null=False,
        blank=False,
        verbose_name='text',
    )
    created_at = models.DateTimeField(
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
        null=True,
        blank=True
    )

    def __str__(self):
        return 'Card: %s' % self.id

    class Meta:
        abstract=True
        ordering = ['-created_at']


class ArticleCard(Card):
    """ArticleCard Model"""

    article = models.ForeignKey(
        Article,
        verbose_name='Article',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        null=False,
        blank=True,
        verbose_name='text'
    )
    date_visible = models.BooleanField(
        default=True,
        blank=True,
        verbose_name='Date is Visible'
    )

    def save(self, *args, **kwargs):
        self.created_at = Article.objects.get(pk=self.article.id).created_at

        if not self.text:
            self.text = Article.objects.get(pk=self.article.id).content
            self.text = Truncator(self.text).words(apps.get_app_config('blog')
                                                   .CARD_TRUNCATE_SIZE)

        super(ArticleCard, self).save(*args, **kwargs)


class BannerCard(Card):

    title = models.CharField(
        max_length=120,
        verbose_name='Title'
    )


class QuoteCard(Card):
    """QuoteCard Model"""

    footer = models.CharField(
        max_length=120,
        verbose_name='Footer'
    )


class ImageCard(Card):

    title = models.CharField(
        null=True,
        max_length=120,
        verbose_name='Title'
    )
    text = models.TextField(
        null=True,
        blank=True,
        verbose_name='text'
    )
    image = models.ImageField(
        upload_to='card-images/%Y/'
    )
