from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from template.forms import TemplateForm, TemplateDataForm
from template.models import Template
from django.contrib.auth.decorators import login_required 


# Create your views here.


# class CheckListView(CreateView):
# 	template_name = 'template/checklist.html'
# 	form_class = TemplateForm
# 	success_url = reverse_lazy('checklist')
# 	# context_object_name = 'obj'

# 	# def form_valid(self, form):
# 	# 	return super().form_valid(form)

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['template'] = Template.objects.all()
# 		return context


@login_required
def template_view(request):
	# Temporary Display of the template names 
	template = Template.objects.filter(user=request.user)

	if request.method == 'POST':
		temp_form = TemplateForm(request.POST)
		temp_data_form = TemplateDataForm(request.POST)

		if temp_form.is_valid() and temp_data_form.is_valid():
			# Template Title and User
			temp_obj = temp_form.save(commit=False)
			temp_obj.user = request.user
			temp_obj.save()

			# Template items alias data
			td_obj = temp_data_form.save(commit=False)
			td_obj.template = temp_obj
			td_obj.save()

			return HttpResponseRedirect(reverse('checklist'))

	else:
		temp_form = TemplateForm()
		temp_data_form = TemplateDataForm()

	return render(request, 'template/checklist.html', locals())
