from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers
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
		print(request.POST)

		if request.POST.get('id'):
			# getting id of the current template 
			existing_template = Template.objects.filter(id=request.POST.get('id'))[0]

		if existing_template:
			existing_template.title = request.POST.get('title')
			existing_template.save()

		elif temp_form.is_valid():
			# Template Title and User
			latest_template_obj = temp_form.save(commit=False)
			latest_template_obj.user = request.user
			latest_template_obj.save()
			# ser_instance = serializers.serialize('json',[temp_obj, ])

			# return JsonResponse({'instance':ser_instance}, status=200)


			# return HttpResponseRedirect(reverse('checklist'))

		elif temp_data_form.is_valid():
			
			# Template items alias data
			td_obj = temp_data_form.save(commit=False)
			td_obj.template = existing_template
			td_obj.save()

			return HttpResponseRedirect(reverse('checklist'))

	else:
		
		temp_data_form = TemplateDataForm()
		if template.filter(title='Untitled'):
			temp_obj_for_template = template.filter(title='Untitled')[0]
			temp_form = TemplateForm(instance=temp_obj_for_template)

		else:
			temp_obj_for_template = Template.objects.create(title='Untitled', user=request.user)
			temp_form = TemplateForm(instance=temp_obj_for_template)

	return render(request, 'template/checklist.html', locals())


def home_view(request):

	return render(request, 'template/home.html')
