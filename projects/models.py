from django.db import models


class SkillStack(models.Model):
    icon = models.ImageField(upload_to="icon/")
    skill_name = models.CharField()


class ImageSet(models.Model):
    image = models.ImageField(upload_to="project_image/")


class Project(models.Model):
    project_name = models.CharField()
    skill_stack = models.ManyToManyField(SkillStack, blank=True, related_name="skills")
    images = models.ForeignKey(ImageSet, on_delete=models.CASCADE, related_name="image_set")
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
