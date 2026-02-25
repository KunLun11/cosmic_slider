from django.db import models

from base.models.bases import BaseModelIDTime
from filer.fields.image import FilerImageField


class Slider(BaseModelIDTime):
    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"
        ordering = ["order"]

    title = models.CharField("Название", max_length=125)
    image = FilerImageField(
        verbose_name="Изображение",
        null=True,
        blank=True,
        related_name="slider_images",
        on_delete=models.SET_NULL,
    )
    order = models.PositiveIntegerField("Порядок сортировки", default=0, db_index=True)
    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.title
