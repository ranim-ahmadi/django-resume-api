import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Resume, Experience, Education, Skill
from .factories import ResumeFactory, ExperienceFactory, EducationFactory, SkillFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def resume():
    return ResumeFactory()


@pytest.mark.django_db
class TestResumeModel:
    def test_create_resume(self):
        resume = ResumeFactory()
        assert resume.id is not None
        assert resume.title is not None

    def test_str_method(self, resume):
        assert str(resume) == resume.title


@pytest.mark.django_db
class TestResumeAPI:
    def test_list_resumes(self, api_client, resume):
        url = reverse('resume-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert 'results' in response.data

    def test_create_resume(self, api_client):
        url = reverse('resume-list')
        data = {
            'title': 'Senior Python Developer',
            'full_name': 'Jean Dupont',
            'email': 'jean.dupont@email.com',
            'summary': 'Experienced Python developer with 8 years expertise in Django and REST APIs'
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Resume.objects.count() == 1

    def test_retrieve_resume(self, api_client, resume):
        url = reverse('resume-detail', args=[resume.id])
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == resume.title

    def test_update_resume(self, api_client, resume):
        url = reverse('resume-detail', args=[resume.id])
        data = {'title': 'Lead Python Developer'}
        response = api_client.patch(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        resume.refresh_from_db()
        assert resume.title == 'Lead Python Developer'

    def test_delete_resume(self, api_client, resume):
        url = reverse('resume-detail', args=[resume.id])
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Resume.objects.count() == 0

    def test_filter_by_email(self, api_client, resume):
        url = reverse('resume-list')
        response = api_client.get(url, {'email': resume.email})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1

    def test_search_by_name(self, api_client, resume):
        url = reverse('resume-list')
        response = api_client.get(url, {'search': resume.full_name.split()[0]})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) >= 1


@pytest.mark.django_db
class TestExperienceAPI:
    def test_list_experiences(self, api_client, resume):
        ExperienceFactory.create_batch(3, resume=resume)
        url = reverse('resume-experiences', args=[resume.id])
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

    def test_add_experience(self, api_client, resume):
        url = reverse('resume-experiences', args=[resume.id])
        data = {
            'company': 'Google',
            'position': 'Senior Python Developer',
            'start_date': '2023-01-01',
            'description': 'Leading backend development team, designing REST APIs',
            'current': True,
            'end_date': None
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert resume.experiences.count() == 1

    def test_validation_end_date_after_start_date(self, api_client, resume):
        url = reverse('resume-experiences', args=[resume.id])
        data = {
            'company': 'Google',
            'position': 'Developer',
            'start_date': '2024-01-01',
            'end_date': '2023-01-01',
            'description': 'Invalid date range',
            'current': False
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestEducationAPI:
    def test_list_education(self, api_client, resume):
        EducationFactory.create_batch(2, resume=resume)
        url = reverse('resume-education', args=[resume.id])
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_add_education(self, api_client, resume):
        url = reverse('resume-education', args=[resume.id])
        data = {
            'institution': 'École Polytechnique',
            'degree': 'Master of Science',
            'field_of_study': 'Computer Science',
            'start_date': '2020-09-01',
            'end_date': '2022-06-30',
            'current': False
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert resume.educations.count() == 1


@pytest.mark.django_db
class TestSkillAPI:
    def test_list_skills(self, api_client, resume):
        SkillFactory.create_batch(3, resume=resume)
        url = reverse('resume-skills', args=[resume.id])
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

    def test_add_skill(self, api_client, resume):
        url = reverse('resume-skills', args=[resume.id])
        data = {
            'name': 'Python',
            'proficiency': 5
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert resume.skills.count() == 1

    def test_validation_proficiency_range(self, api_client, resume):
        url = reverse('resume-skills', args=[resume.id])
        data = {
            'name': 'Python',
            'proficiency': 10
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST