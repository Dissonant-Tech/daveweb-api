from django.db import models

from django.conf import settings


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
        max_length=255
    )
    content = models.TextField(
        verbose_name='Content (Markdown)',
    )
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
    """Card Model"""
    title = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        verbose_name='Title'
    )
    text = models.TextField(
        null=True,
        verbose_name='text',
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='card-images/%Y/'
    )
    link = models.URLField(
        null=True,
        blank=True
    )
    classes = models.CharField(
        max_length=200,
        null=True
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
    article = models.ForeignKey(
        Article,
        verbose_name='Article',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name='Categories',
        blank=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='User'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return 'Card: %s' % self.id
