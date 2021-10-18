from django.db import models
from django.db.models import Count


class ThreadManager(models.Manager):
    def get_or_create_personal_thread(self, user1, user2):
        print("checking thread.....")
        threads = self.get_queryset().filter(thread_type='personal')
        threads = threads.filter(users__in=[user1, user2]).distinct()
        threads = threads.annotate(u_count=Count('users')).filter(u_count=2)
        if threads.exists():
            print("thread Already Exist")
            return threads.first()
        else:
            print("creating new thread")
            thread = self.create(thread_type='personal')
            thread.users.add(user1)
            thread.users.add(user2)
            return thread

    def by_user(self, user):
        return self.get_queryset().filter(users__in=[user])

    def checking_thread_existence(self, user1, user2):
        print("checking thread.....")
        threads = self.get_queryset().filter(thread_type='personal')
        threads = threads.filter(users__in=[user1, user2]).distinct()
        threads = threads.annotate(u_count=Count('users')).filter(u_count=2)
        if threads.exists():
            print("thread Already Exist")
            return threads.first()
        else:
            return None