from http.client import HTTPResponse
from django.shortcuts import render, redirect

from blog.forms import CommentForm
from .models import Post

def frontpage(request):
    """
    フロントのページを表示する
    Args:
        request (HttpRequest): リクエスト
    Returns:
        HttpResponse: レスポンス
    """
    posts = Post.objects.all()
    print(f'posts内容：{posts}')
    return render(request, "blog/frontpage.html", {"posts": posts})

def post_detail(request, slug):
    """
    詳細ページを表示する
    Args:
        request (HttpRequest): リクエスト
        slug (str): スラッグ
    Returns:
        HttpResponse: レスポンス
    """
    post = Post.objects.get(slug=slug)
    # フォームの送信があった場合
    if request.method == "POST":
        # フォームの内容をrequest.POSTから取得
        form = CommentForm(request.POST)

        # is_valid()でフォームの内容のバリデーションを実行
        if form.is_valid():
            # バリデーションに成功した場合、フォームの内容を保存
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            # 現在の詳細ページにリダイレクト
            return redirect("post_detail", slug=post.slug)
    else:
        # CommentForm()で空のフォームを作成
        form = CommentForm()

    return render(request, "blog/post_detail.html", {"post": post, "form": form})