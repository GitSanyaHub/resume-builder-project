from django.contrib.auth.models import AbstractUser, User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Resume(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE, null=True)

    title = models.CharField("Название резюме", blank=True, max_length=255, default="Программист .Net")
    first_name = models.CharField("Имя", max_length=50, blank=True)
    last_name = models.CharField("Фамилия", max_length=50, blank=True)
    address = models.CharField("Адрес", max_length=255, blank=True, default="город Москва")
    phone = models.CharField("Телефон", max_length=25, blank=True, default="8 999 999 99 99")
    email_two = models.EmailField("Email", blank=True, max_length=25, default="example@mail.ru")
    content = models.TextField("О вас", blank=True, default="Кто Я?")
    photo = models.ImageField("Аватар", blank=True, null=True, upload_to="photos/%Y/%m/%d/")

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField('Последнее обновление', auto_now=True)
    is_pub = models.BooleanField(default=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"




    @receiver(post_save, sender=User)
    def save_or_create_resume(sender, instance, created, **kwargs):
        if created:
            Resume.objects.create(user=instance, pk=instance.pk)
        else:
            try:
                instance.resume.save()
            except ObjectDoesNotExist:
                Resume.objects.create(user=instance)