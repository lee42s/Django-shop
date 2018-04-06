from member.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','nickname','gender','zipCode','address','detailedAddress','phone_nember']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username', 'placeholder':'8자 이내로 입력 가능합니다.'}),
            'nickname': forms.TextInput(attrs={'class': 'nickname', 'placeholder': '5자 이내로 입력 가능합니다.'}),
            'phone_nember': forms.TextInput(attrs={'class': 'nickname', 'placeholder': '000-0000-0000'}),
        }
        labels = {
            'username': '아이디',
            'email': '이메일',
            'nickname':'닉네임',
            'gender':'성별',
            'zipCode':'우편주소',
            'address':'기본주소',
            'detailedAddress':'상세주소',
            'phone_nember':'폰번호',
        }
    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__( *args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 8
        self.fields['nickname'].widget.attrs['maxlength'] = 5





