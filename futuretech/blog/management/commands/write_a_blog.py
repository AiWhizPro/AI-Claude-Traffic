from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

from blog.models import BlogPost
from claude_integration import generate_claude_response


class Command(BaseCommand):
    help = (
        'Generate and publish a blog post from a comparison keyword using Claude AI. '
        'The generated post is saved as a published BlogPost and will appear on the homepage.'
    )

    def add_arguments(self, parser):
        parser.add_argument(
            'comparison_keyword',
            help='A comparison keyword phrase in the form "X vs Y".',
        )
        parser.add_argument(
            '--slug',
            help='Optional slug to use for the generated post. Defaults to a slugified keyword.',
        )
        parser.add_argument(
            '--model',
            default='claude-3.5',
            help='Anthropic Claude model name to use for generation.',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Generate the page but do not save it to the database.',
        )

    def handle(self, *args, **options):
        comparison_keyword = options['comparison_keyword'].strip()
        if not comparison_keyword:
            raise CommandError('Please provide a comparison keyword phrase such as "Cursor vs Copilot".')

        slug = options['slug'] or slugify(comparison_keyword)
        if not slug:
            raise CommandError('Could not generate a slug from the comparison keyword.')

        slug = self._make_unique_slug(slug)
        title = f'{comparison_keyword} — Honest Comparison'

        prompt = (
            'Use the BlogSkill instructions from BlogSkill.md to create a complete, publish-ready HTML '
            'comparison article for the keyword "' + comparison_keyword + '". '
            'Output a full HTML page only, including <head>, schema JSON-LD, hero, TOC, quick verdict, '
            'Reddit-style community quotes, head-to-head table, pricing section, scenario cards, third-option CTA, FAQ, and footer. '
            'Keep sentences short, active voice, and make the page ready to publish on the homepage of aiwhizpro.com.'
        )

        self.stdout.write('Generating blog post with Claude...')
        html = generate_claude_response(prompt, model=options['model'], max_tokens=1800)

        if not html or not html.strip():
            raise CommandError('Claude returned no content. Check your API key and prompt.')

        if options['dry_run']:
            self.stdout.write(html)
            return

        post = BlogPost.objects.create(
            title=title,
            slug=slug,
            comparison_keyword=comparison_keyword,
            content=html,
            published=True,
        )

        self.stdout.write(self.style.SUCCESS(
            f'Published blog post: "{post.title}" (slug={post.slug}).\n'
            'It will appear on the homepage automatically.'
        ))

    def _make_unique_slug(self, base_slug):
        slug = base_slug
        counter = 1
        while BlogPost.objects.filter(slug=slug).exists():
            counter += 1
            slug = f'{base_slug}-{counter}'
        return slug
