from django.db import models


class SkillStack(models.Model):
    #    icon = models.ImageField(upload_to="icon/")
    skill_name = models.CharField(max_length=50)


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    skill_stack = models.ManyToManyField(SkillStack, blank=True, related_name="skills")
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()


class ImageSet(models.Model):
    image = models.ImageField(upload_to="project_image/")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
