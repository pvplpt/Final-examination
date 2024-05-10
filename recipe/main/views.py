from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.core.paginator import Paginator
from .models import AdvUser, Category, Rs
from .forms import ChangeUserInfoForm, RegisterUserForm
from .forms import SearchForm, RsForm

class RSLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'

class RSLoginView(LoginView):
    template_name = 'main/login.html'

def by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    rss = Rs.objects.filter(category=pk)
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(title__icontains=keyword) | Q(description__icontains=keyword)
        rss = rss.filter(q)
    else:
        keyword = ''
    form = SearchForm(initial={'keyword':keyword})
    paginator = Paginator(rss, 5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'category': category, 'page': page, 'rss': page.object_list, 'form': form}
    return render(request, 'main/by_category.html', context)


def other_page(request,page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

def index(request):
    no_random = False
    rss = []
    if request.user.is_authenticated:
        adv_user = AdvUser.objects.get(pk=request.user.pk)
        no_random = adv_user.send_messages
    if no_random:
        rss = Rs.objects.all()[:5]
    else:
        rss = Rs.objects.all().order_by('?')[:5]
    context = {'rss': rss, 'no_random': no_random}
    return render(request,'main/index.html', context)

@login_required
def profile(request):
    rss = Rs.objects.filter(author=request.user.pk)
    context = {'rss': rss}
    return render(request, 'main/profile.html', context)

class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class RSPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль пользователя изменен'

class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')

class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'

class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:index')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
        return super().post(request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

def detail(request, category_pk, pk):
    rs = get_object_or_404(Rs, pk=pk)
    context = {'rs': rs}
    return render(request, 'main/detail.html', context)

@login_required
def profile_rs_detail(request, pk):
    rs = get_object_or_404(Rs, pk=pk)
    context = {'rs': rs}
    return render(request, 'main/profile_rs_detail.html', context)

@login_required
def profile_rs_add(request):
    if request.method == 'POST':
        form = RsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Рецепт добавлен')
            return redirect('main:profile')
    else:
        form = RsForm(initial={'author': request.user.pk})
    context = {'form': form}
    return render(request, 'main/profile_rs_add.html', context)

@login_required
def profile_rs_change(request, pk):
    rs = get_object_or_404(Rs, pk=pk)
    if request.method == 'POST':
        form = RsForm(request.POST, request.FILES, instance=rs)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Рецепт изменен')
            return redirect('main:profile')
    else:
        form = RsForm(instance=rs)
    context = {'form': form}
    return render(request, 'main/profile_rs_change.html', context) 

@login_required
def profile_rs_delete(request, pk):
    rs = get_object_or_404(Rs, pk=pk)
    if request.method == 'POST':
        rs.delete()
        messages.add_message(request, messages.SUCCESS, 'Рецепт удален')
        return redirect('main:profile')
    else:
        context = {'rs': rs}
        return render(request, 'main/profile_rs_delete.html', context) 

def all_recipes(request):
    rss = Rs.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(title__icontains=keyword) | Q(description__icontains=keyword)
        rss = rss.filter(q)
    else:
        keyword = ''
    form = SearchForm(initial={'keyword':keyword})
    paginator = Paginator(rss, 5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'page': page, 'rss': page.object_list, 'form': form}
    return render(request, 'main/all_recipes.html', context)

def all_recipes_detail(request, pk):
    rs = get_object_or_404(Rs, pk=pk)
    context = {'rs': rs}
    return render(request, 'main/all_recipes_detail.html', context)