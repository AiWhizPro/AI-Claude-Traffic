from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.decorators.http import require_http_methods
from .models import BlogPost
from .forms import BlogPostForm


def home(request):
    qs = BlogPost.objects.filter(published=True).order_by('-created_at')
    # Deduplicate by slug while preserving order to avoid duplicate cards
    seen = set()
    unique_posts = []
    for p in qs:
        if p.slug in seen:
            continue
        seen.add(p.slug)
        unique_posts.append(p)

    total = len(unique_posts)
    limit = 6
    posts = unique_posts[:limit]
    more_available = total > limit
    return render(request, 'blog/home.html', {
        'posts': posts,
        'total_posts': total,
        'more_available': more_available,
    })


def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})


def posts_menu(request):
    """Menu page listing all published posts (paginated simple view)."""
    posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/menu.html', {'posts': posts})


@require_http_methods(["GET", "POST"])
def admin_posts(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    if request.method == 'POST' and 'delete_id' in request.POST:
        post_id = request.POST.get('delete_id')
        try:
            post = BlogPost.objects.get(id=post_id)
            post.delete()
            return redirect('blog:admin_posts')
        except BlogPost.DoesNotExist:
            pass
    return render(request, 'blog/admin_posts.html', {'posts': posts})


@require_http_methods(["GET", "POST"])
def admin_post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('blog:admin_posts')
    else:
        form = BlogPostForm()
    return render(request, 'blog/admin_post_form.html', {'form': form, 'title': 'Create New Post'})


@require_http_methods(["GET", "POST"])
def admin_post_edit(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:admin_posts')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/admin_post_form.html', {
        'form': form,
        'post': post,
        'title': f'Edit: {post.title}'
    })
