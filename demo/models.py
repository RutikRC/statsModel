from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class stepsModel(models.Model):
     # Choices for the steps field
    PROJECT_START = 'project_start'
    STRUCTURAL_WORK = 'structural_work'
    LAMINATE_WORK = 'laminate_work'
    HARDWARE_INSTALL = 'hardware_install'
    FURNISHING_WORK = 'furnishing_work'
    HAND_OVER_AND_FINALIZING = 'hand_over_and_finalizing'

    STEP_CHOICES = [
        (PROJECT_START, 'Project Start'),
        (STRUCTURAL_WORK, 'Structural Work'),
        (LAMINATE_WORK, 'Laminate Work'),
        (HARDWARE_INSTALL, 'Hardware Installation'),
        (FURNISHING_WORK, 'Furnishing Work'),
        (HAND_OVER_AND_FINALIZING, 'Hand Over and Finalizing'),
    ]

    model_name = models.CharField(max_length = 50, choices=STEP_CHOICES, default=PROJECT_START)
    Status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f'{self.id}-{self.model_name}-{self.Status}'
    
class imgTitleStructuralWork(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='execution_work_images/')  # You might want to adjust the upload_to path
    stepsmodel = models.ForeignKey(stepsModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.stepsmodel}"