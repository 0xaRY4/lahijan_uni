from django import forms
from .models import Faculty

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'academic_rank', 'department', 'education', 'research_interests', 'email', 'phone', 'profile_image', 'resume_file']