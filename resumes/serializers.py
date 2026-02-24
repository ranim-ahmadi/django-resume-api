from rest_framework import serializers
from .models import Resume, Experience, Education, Skill

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        read_only_fields = ['id']

    # Validation: end_date must be after start_date
    def validate(self, data):
        if data.get('end_date') and data['end_date'] < data['start_date']:
            raise serializers.ValidationError("End date must be after start date")
        if data.get('current') and data.get('end_date') is not None:
            raise serializers.ValidationError("If current is True, end_date should be null")
        return data


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        read_only_fields = ['id']

    # Validation: end_date must be after start_date
    def validate(self, data):
        if data.get('end_date') and data['end_date'] < data['start_date']:
            raise serializers.ValidationError("End date must be after start date")
        if data.get('current') and data.get('end_date') is not None:
            raise serializers.ValidationError("If current is True, end_date should be null")
        return data


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        read_only_fields = ['id']

    # Validation: proficiency must be between 1-5
    def validate_proficiency(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Proficiency must be between 1 and 5")
        return value


class ResumeSerializer(serializers.ModelSerializer):
    # Nested serialization for related data
    experiences = ExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = ['id', 'title', 'full_name', 'email', 'phone', 'summary',
                 'created_at', 'updated_at', 'experiences', 'educations', 'skills']
        read_only_fields = ['id', 'created_at', 'updated_at']

    # Validation: email is already validated by EmailField