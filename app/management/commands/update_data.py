from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.tasks import update_play_history


class Command(BaseCommand):
    help = 'Updates recent play history data for all members'

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            update_play_history(user) if hasattr(user, 'oh_member') else None
