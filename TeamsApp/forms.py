from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Team, GameScore, Player


class AddTeamForm(forms.Form):

    Name_1 = forms.CharField(
        label='اسم الفريق',
        required=True,
    )

    Details_1 = forms.CharField(
        label='التفاصيل'
    )

class AddTeamModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddTeamModelForm , self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:

        model = Team
        fields = '__all__'
        labels = {
            'name': 'اسم الفريق',
            'details': 'تفاصيل الفريق',
        }

        error_messages = {
            'name': {
                'unique': 'هذا الفريق موجود مسبقاً في قاعدة البيانات'
            }
        }


class AddScore(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddScore , self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = GameScore
        exclude = ['date']
        labels = {
            'team1': "الفريق الأول",
            'team2': 'الفريق الثاني',
            'first_team_score': 'نتيجة الفريق الأول',
            'second_team_score': 'نتيجة الفريق الثاني',
        }


class AddPlayerModelForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(AddPlayerModelForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper(self)

        class Meta:
            model = Player
            fields = '__all__'
            labels = {
                'name': 'اسم الاعب',
                'age': 'العمر',
                'number': 'الرقم',
                'position_in_field': 'موضعه في الملعب',
                'is_captain': 'قائد الفريق',
                'team': 'الفريق',
            }

