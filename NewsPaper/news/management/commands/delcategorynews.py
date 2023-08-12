from django.core.management.base import BaseCommand

from NewsPaper.news.models import Post, Category


class Command(BaseCommand):
    help = 'Удаление всех новостей категории.'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        self.stdout.write('Вы действительно хотите удалить все новости категории? yes/no')
        answer = input(f'Вы действительно хотите удалить все новости категории {options["category"]}? yes/no')
        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Удаление отменено!'))
            return
        try:
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Новости в категории {category.name} успешно удалены!'))
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Не удалось найти категорию {options["category"]}!'))
