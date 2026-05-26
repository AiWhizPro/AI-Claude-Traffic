from django.test import TestCase
from django.urls import reverse
from .models import BlogPost


class BlogViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.published_posts = []
        for index in range(7):
            cls.published_posts.append(
                BlogPost.objects.create(
                    title=f"Post {index + 1}",
                    slug=f"post-{index + 1}",
                    comparison_keyword=f"Keyword {index + 1}",
                    content=f"<p>Content for post {index + 1}</p>",
                    published=True,
                )
            )
        cls.unpublished_post = BlogPost.objects.create(
            title="Unpublished Post",
            slug="unpublished-post",
            comparison_keyword="Hidden Keyword",
            content="<p>Hidden content</p>",
            published=False,
        )

    def test_home_displays_only_six_posts_and_shows_more_available(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('posts', response.context)
        self.assertIn('more_available', response.context)
        self.assertEqual(len(response.context['posts']), 6)
        self.assertTrue(response.context['more_available'])
        self.assertContains(response, 'View all posts')
        self.assertNotContains(response, 'No posts yet')

    def test_posts_menu_lists_all_published_posts(self):
        response = self.client.get(reverse('blog:menu'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('posts', response.context)
        self.assertEqual(len(response.context['posts']), len(self.published_posts))
        for post in self.published_posts:
            self.assertContains(response, post.title)

    def test_post_detail_returns_404_for_unpublished_post(self):
        response = self.client.get(reverse('blog:post_detail', kwargs={'slug': self.unpublished_post.slug}))
        self.assertEqual(response.status_code, 404)
