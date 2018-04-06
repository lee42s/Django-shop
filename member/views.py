from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from member.forms import CreateUserForm
from django.contrib.auth import login
from member.models import User
from django.urls import reverse_lazy
from django.http import JsonResponse
# Create your views here.
class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('home')


# get 방식
def validate_username(request):
    # HttpRequest 객체의 GET 과 POST 속성은 django.http.QueryDict 의 인스턴스입니다.
    # get()메서드는 키(여기서는 username)이 없는 경우 기본값 'None'을 반환합니다. https://goo.gl/wtA6KN
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)

    data = {
        # <필드명>__iexact는 대소문자를 구분하지 않고 일치하는 값을 찾는다. https://goo.gl/5XywcT
        # exists()는 쿼리셋에 결과가 있는 경우 True를 반환합니다. https://goo.gl/Vgtr2u
        'is_taken_username':User.objects.filter(username__iexact = username).exists()

    }
    if data['is_taken_username']:
        data['error_message'] = '아이디가 이미 존재합니다. 다른 이름을 입력해 주세요.'

    # data를 Json형식으로 인코딩되도록 합니다.
    return JsonResponse(data)


