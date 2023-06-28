from random import choice, sample, randint

from django.core.management.base import BaseCommand
from faker import Faker

from orders.models import UserFeedback, Source, UserFeedbackService
from services.models import SubService


class Command(BaseCommand):
    help = 'Create random user feedbacks'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of user feedbacks to be created')

    def handle(self, *args, **kwargs):
        fake = Faker()

        sources = Source.objects.all()

        services = SubService.objects.all()

        total = kwargs['total']
        for _ in range(total):
            name = fake.name()
            phone = fake.phone_number()[:20]

            source = choice(sources)

            feedback = UserFeedback.objects.create(
                name=name,
                phone=phone,
                source=source
            )
            num_services = randint(1, 5)
            selected_services = sample(list(services), num_services)
            for service in selected_services:
                UserFeedbackService.objects.create(feedback=feedback, service=service)

            self.stdout.write(self.style.SUCCESS(f'Successfully created user feedback with id {feedback.id}'))
