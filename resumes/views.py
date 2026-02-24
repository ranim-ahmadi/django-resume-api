from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Resume, Experience, Education, Skill
from .serializers import (
    ResumeSerializer, ExperienceSerializer,
    EducationSerializer, SkillSerializer
)


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['email']  # Filtering by email
    search_fields = ['full_name', 'title']  # Search by full_name or title
    ordering_fields = ['created_at', 'updated_at']  # Ordering by created_at or updated_at

    @action(detail=True, methods=['get', 'post'])
    def experiences(self, request, pk=None):
        resume = self.get_object()

        if request.method == 'GET':
            experiences = resume.experiences.all()
            serializer = ExperienceSerializer(experiences, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = ExperienceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(resume=resume)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get', 'post'])
    def education(self, request, pk=None):
        resume = self.get_object()

        if request.method == 'GET':
            education = resume.educations.all()
            serializer = EducationSerializer(education, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = EducationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(resume=resume)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get', 'post'])
    def skills(self, request, pk=None):
        resume = self.get_object()

        if request.method == 'GET':
            skills = resume.skills.all()
            serializer = SkillSerializer(skills, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = SkillSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(resume=resume)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
