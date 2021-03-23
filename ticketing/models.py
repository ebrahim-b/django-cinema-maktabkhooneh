from django.db import models

class Movie(models.Model):

    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم'

    name = models.CharField('عنوان', max_length = 100)
    director =  models.CharField('کارگردان', max_length = 50)
    year = models.IntegerField('سال ساخت')
    length = models.IntegerField('زمان')
    description = models.TextField('توضیحات')

    def __str__(self):
        return self.name


class Cinema(models.Model):

    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'

    cinema_code = models.IntegerField('کد', primary_key = True)
    name = models.CharField('نام', max_length = 50)
    city = models.CharField('شهر', max_length = 30, default = 'تهران')
    capacity = models.IntegerField('ظرفیت')
    phone = models.CharField('تلفن', max_length = 20, null=True)
    address = models.TextField('آدرس')

    def __str__(self):
        return self.name


class ShowTime(models.Model):

    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس'

    movie = models.ForeignKey('Movie', on_delete = models.PROTECT, verbose_name = 'فیلم')
    cinema = models.ForeignKey('Cinema', on_delete=models.PROTECT, verbose_name = 'سینما')
    start_time = models.DateTimeField('زمان شروع')
    price = models.IntegerField('قیمت')
    salable_seats = models.IntegerField('صندلی های قابل فروش')
    free_seats = models.IntegerField('صندلی های خالی')

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = (
        (SALE_NOT_STARTED, 'فروش آغاز نشده'),
        (SALE_OPEN, 'در حال فروش بلیت'),
        (TICKETS_SOLD, 'بلیت ها تمام شد'),
        (SALE_CLOSED, 'فروش بلیت بسته شد'),
        (MOVIE_PLAYED, 'فیلم پخش شد'),
        (SHOW_CANCELED, 'سانس لغو شد'),
    )

    status = models.IntegerField('وضعیت', choices=status_choices)

    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.cinema, self.start_time)