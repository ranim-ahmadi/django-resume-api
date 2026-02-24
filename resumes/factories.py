import factory
from factory.django import DjangoModelFactory
from factory import Faker
from .models import Resume, Experience, Education, Skill


class ResumeFactory(DjangoModelFactory):
    class Meta:
        model = Resume

    title = Faker('job')
    full_name = Faker('name')
    email = Faker('email')
    summary = Faker('paragraph')
    phone = Faker('phone_number')

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Truncate phone number to max_length 20"""
        if 'phone' in kwargs and kwargs['phone'] and len(kwargs['phone']) > 20:
            kwargs['phone'] = kwargs['phone'][:20]
        return super()._create(model_class, *args, **kwargs)


class ExperienceFactory(DjangoModelFactory):
    class Meta:
        model = Experience

    resume = factory.SubFactory(ResumeFactory)
    company = Faker('company')
    position = Faker('job')
    start_date = Faker('date_this_decade')
    end_date = None
    description = Faker('paragraph')
    current = True


class EducationFactory(DjangoModelFactory):
    class Meta:
        model = Education

    resume = factory.SubFactory(ResumeFactory)
    institution = Faker('company')  # university doesn't exist in Faker
    degree = Faker('word')
    field_of_study = Faker('word')
    start_date = Faker('date_this_decade')
    end_date = None
    current = True


class SkillFactory(DjangoModelFactory):
    class Meta:
        model = Skill

    resume = factory.SubFactory(ResumeFactory)
    name = Faker('word')
    proficiency = Faker('random_int', min=1, max=5)