from django.core.management.base import BaseCommand, CommandError
from accounts.models import Profile
from django.contrib.auth.models import User
import numpy as np

class Command(BaseCommand):
    def handle(self, *args, **options):
        
        names = ['Jakub', 'Antoni', 'Jan', 'Szymon', 'Filip', 'Alexander', 'Wojciech', 'Franciszek', 'Mikołaj', 'Michał']
        surnames = ['Nowak', 'Kowalski', 'Wiśniewski', 'Wójcik', 'Kowalczyk', 'Kamiński', 'Lewandowski']
        for i in range(50):
            user = User.objects.get(id=user_id)
            new_user = Profile()
            new_user.user = user
            new_user.username = 'user'+str(i)
            new_user.email = 'user'+str(i)+'@gmail.com'
            new_user.first_name = names[np.random.randint(len(names)-1)]
            new_user.last_name = surnames[np.random.randint(len(surnames)-1)]
            new_user.save()