# -*- coding: utf-8 -*-

from django.db import models

class Relative(models.Model):
    """Relative's Model"""

    class Meta(object):
        verbose_name = u"Родич"
        verbose_name_plural = u"Родичі"

    first_name = models.CharField(
        max_length="100",
        blank=False,
        verbose_name=u"Ім’я"
    )

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Прізвище",
    )

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"По-батькові",
        default=''
    )

    birthday = models.DateField(
        blank=False,
        verbose_name=u"Дата народження",
        null=True
    )

    photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True
    )

    sex = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Стать",
        choices=(
            (u'Чоловіча', u'Чоловіча'),
            (u'Жіноча', u'Жіноча'),
        )
    )

    generation = models.SmallIntegerField(
        blank=True,
        verbose_name=u"Покоління №",
        null=True
    )

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки"
    )

    father = models.OneToOneField("self", blank=True, related_name="dad")
    mother = models.OneToOneField("self", blank=True, related_name="mom")

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)