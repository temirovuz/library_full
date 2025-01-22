from django.db import models
from django.db.models import CASCADE


# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(Base):
    name = models.CharField(max_length=255, unique=True)
    cleaned_name = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.cleaned_name = re.sub(r"[^a-zA-Z0-9\s]", "", self.name).lower().strip()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(Base):
    name = models.CharField(max_length=255, unique=True)
    cleaned_name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.cleaned_name = re.sub(r"[^a-zA-Z0-9\s]", "", self.name).lower().strip()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['name']

    def __str__(self):
        return self.name


class Language(Base):
    lang = models.CharField(max_length=255, unique=True)
    cleaned_lang = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.cleaned_lang = re.sub(r"[^a-zA-Z0-9\s]", "", self.name).lower().strip()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ['lang']

    def __str__(self):
        return self.lang


class Book(Base):
    name = models.CharField(max_length=255)
    cleaned_name = models.CharField(max_length=255)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    publication_date = models.DateField(null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books')
    language = models.ForeignKey(Language, on_delete=CASCADE)
    daily_price = models.DecimalField(max_digits=10, decimal_places=2)
    available_copies = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.cleaned_name = re.sub(r"[^a-zA-Z0-9\s]", "", self.name).lower().strip()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['name']

    def __str__(self):
        return self.name

    def display_authors(self):
        """Create a string for the Authors. This is required to display authors in Admin."""
        return ', '.join([author.__str__() for author in self.authors.all()[:3]])

    def display_genres(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genres.all()[:3]])

    display_authors.short_description = 'Authors'
    display_genres.short_description = 'Genres'
