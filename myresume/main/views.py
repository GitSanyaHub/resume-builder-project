import pdfkit
from django.contrib import messages
from django.contrib.auth import logout, login
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from main.forms import LoginUserForm, RegisterUserForm
from main.models import Resume
from myresume import settings


def index(request):
    return render(request, 'index.html')


class UpdateResumeView(UpdateView):
    model = Resume

    template_name = 'create_resume.html'
    fields = ['title', 'first_name', 'last_name', 'address', 'phone', 'email_two', 'email_two', 'email_two', 'content',
              'photo']

    # def form_valid(self, form):
    #     form.save = self.request.user
    #     return super().form_valid(form)

    success_url = reverse_lazy('main')


class ResumeDetail(DetailView):
    model = Resume
    template_name = 'resume-detail.html'

    fields = ['user', 'title', 'first_name', 'last_name', 'address', 'phone', 'email_two', 'email_two', 'email_two', 'content',
              'photo', 'time_update']

    def get_context_data(self, *args, **kwargs):
        users = Resume.objects.all()
        context = super(ResumeDetail, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Resume, id=self.kwargs['pk'])
        context['resume'] = page_user
        return context


def pdf(request):
    path_wkhtmltopdf = settings.path_wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    projectUrl = request.get_host() + f'/resume-detail/{request.user.id}'
    pdf = pdfkit.from_url(projectUrl, False, configuration=config)
    # Generate download
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resume_{request.user.resume.title}.pdf"'

    return response


def user_login(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
        else:
            messages.warning(request, 'НЕ успешно!')
    else:
        form = LoginUserForm()

    return render(request, 'login.html', context={'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Успешно')
            login(request, user=user)
            return redirect('main')
        else:
            messages.error(request, 'Ошибка!')
    else:
        form = RegisterUserForm()
    context = {
        'form': form
    }

    return render(request, 'register.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')