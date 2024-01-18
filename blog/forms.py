from django import forms
from .models import Comment


# ModelFormを継承したクラスを作成することで、モデルのフィールドをフォームのフィールドとして利用できる
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 属性 = [フィールド名, ...]
        fields = ["name", "email", "body"]