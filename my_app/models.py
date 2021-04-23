from django.db import models


class Tema(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "tem's"

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text


class Razdel(models.Model):
    """Информация, изученная пользователем по теме"""
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'razdely'

    def __str__(self):
        """Возвращает стороковое представление модели"""
        if len(self.text.__str__()) > 50:
            return f"{self.text[:50]}..."

        return self.text.__str__()