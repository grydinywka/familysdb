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

    father = models.ForeignKey("self", blank=True, null=True, related_name="children_dad")
    mother = models.ForeignKey("self", blank=True, null=True, related_name="children_mom")

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

class Surname(models.Model):
    DAD_SIDE = u"по-батьку"
    MOM_SIDE = u"по-мамі"
    SIDE_MOM_DAD = (
        (DAD_SIDE, u"по-батьку"),
        (MOM_SIDE, u"по-мамі"),
    )

    class Meta(object):
        verbose_name = u"Прізвище"
        verbose_name_plural = u"Прізвища"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Прізвище",
    )

    side = models.CharField(
        max_length=9,
        blank=False,
        choices=SIDE_MOM_DAD,
        default= DAD_SIDE
    )

    def __unicode__(self):
        return u"%s" % (self.title)