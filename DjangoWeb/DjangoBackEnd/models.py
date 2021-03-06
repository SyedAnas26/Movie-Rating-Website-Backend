from django.db import models


class MovieRating(models.Model):
    MovieId = models.AutoField(primary_key=True)
    MovieTitle = models.CharField(max_length=100, null=False)
    ReleaseDate = models.DateField(null=False)
    MovieImage = models.ImageField(upload_to='', null=False)
    UpVotes = models.BigIntegerField(default=0)
    DownVotes = models.BigIntegerField(default=0)
    Rating = models.DecimalField(max_digits=5, decimal_places=1, default=0)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


# class Rating(models.Model):
#     MovieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     UpVotes = models.BigIntegerField()
#     DownVotes = models.BigIntegerField()
#     Rating = models.DecimalField(max_digits=5, decimal_places=2)
#
#     class Meta:
#         verbose_name = 'Rating'
#         verbose_name_plural = 'Ratings'
