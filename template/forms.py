from template.models import Template, TempData, CHOICES

from django import forms


class TemplateForm(forms.ModelForm):
	title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Title', 'id':'js_template_title'}))
	class Meta:
		model = Template
		fields = ['title']


class TemplateDataForm(forms.ModelForm):
	status = forms.ChoiceField(label='', choices=CHOICES, widget=forms.TextInput(attrs={"class":"form-control-range ui-slider-handle", "id":"formControlRange"}))
	class Meta:
		model = TempData
		fields = ['item','status']