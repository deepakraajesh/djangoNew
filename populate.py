import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','help.settings')

import django
django.setup()

import random
from helpapp.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Science','News','Technology','Games']

def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top=add_topics()

        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        webpg=Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

        accrd=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating the Values")
    populate()
    print("Script Executed Successfully")
