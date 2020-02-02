from template.models import Template, TempData

from django import forms


class TemplateForm(forms.ModelForm):

	class Meta:
		model = Template
		fields = ['title']


class TemplateDataForm(forms.ModelForm):

	class Meta:
		model = TempData
		fields = ['item','status']