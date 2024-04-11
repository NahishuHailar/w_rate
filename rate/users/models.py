from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Телефон')
    email = models.EmailField(unique=True)
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    city = models.ForeignKey('City', on_delete=models.PROTECT, null=True, verbose_name="Город")

    def __str__(self) -> str:
        return self.username
    

class City(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.title 
    

class Skill(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Навык')
    has_common_title = models.BooleanField()
    common_skill = models.ForeignKey('CommonSkill', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title    


class CommonSkill(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Сфера навыка')

    def __str__(self):
        return self.title


class UserSkillList(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username + ' ' + self.skill.title


class Mark(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill,on_delete=models.PROTECT)
    mark = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.user.username + ' ' + self.skill.title + ' ' + str(self.mark) 


class Portfolio(models.Model):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Фото')
    description = models.CharField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, null=True, blank=True)


    def __str__(self):
        return 'Портфолио ' + self.user.username 
    
