from django import forms

# 기존 폼을 상송받아서 간단하게 주멀럭대준다. 아래와 같이 그리고 views.py에서 적용받아 어떻게 흘러갈지 물꼬를 내준다고 보면됨

class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.' # 제목을 입력하지 않고 글 작성 완료 버튼을 누를 경우 발생
        },
        max_length=128, label="제목") # 제목란에는 128자로 제한, label에는 '제목'이라고 지정함
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.' # '내용' 입력란에 입력하지 않고 글 작성 완료 버튼을 누를 경우 오류 생성 문자
        },
        widget=forms.Textarea, label="내용") # 위젯 옵션은  Textarea로 지정함
    tags = forms.CharField(
        required=False, label="태그")
