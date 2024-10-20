from django.db.models import Max, Count
from django.shortcuts import render
from django.views import View
# from .models import ...
from .models import Author, AuthorProfile, Entry, Tag


class TrainView(View):
    def get(self, request):
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])

        self.answer2 = Author.objects.annotate(num_entries=Count('entries')).order_by('-num_entries').first()
        self.answer3 = Entry.objects.filter(tags__name__in=['Кино', 'Музыка'])
        self.answer4 = Author.objects.filter(gender='ж').count()
        total_authors_count = Author.objects.count()
        agreed_authors_count = Author.objects.filter(status_rule=True).count()

        if total_authors_count > 0:
            percentage_agreed = (agreed_authors_count / total_authors_count) * 100
        else:
            percentage_agreed = 0

        self.answer5 = percentage_agreed
        authors_with_stage = AuthorProfile.objects.filter(stage__gte=1, stage__lte=5)
        self.answer6 = authors_with_stage
        self.answer7 = Author.objects.aggregate(Max('age'))['age__max']
        self.answer8 = Author.objects.filter(phone_number__isnull=False).count()
        self.answer9 = Author.objects.filter(age__lt=25)
        self.answer10 = Author.objects.annotate(num_entries=Count('entries')).order_by('-num_entries')

        context = {
        f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)
        }
        return render(request, 'train_db/training_db.html', context=context)

