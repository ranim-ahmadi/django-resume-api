from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Resume(models.Model):
    title = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)  # optional
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # optional
    description = models.TextField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.position} at {self.company}"

    class Meta:
        ordering = ['-start_date']


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # optional
    current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study}"

    class Meta:
        ordering = ['-start_date']


class Skill(models.Model):
    PROFICIENCY_CHOICES = [
        (1, 'Beginner'),
        (2, 'Elementary'),
        (3, 'Intermediate'),
        (4, 'Advanced'),
        (5, 'Expert'),
    ]

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(choices=PROFICIENCY_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
