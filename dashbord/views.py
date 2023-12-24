from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, FormView
from orders.models import Order
from .forms import ForrmatForm, FormGetDate
from .admin import PostResourse
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from accounts.models import CustomerUser
from datetime import date
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


class HomePage(ListView, FormView):
    template_name = "dashbord/home.html"
    form_class = ForrmatForm
    success_url = reverse_lazy("home:home")


    def get_queryset(self, start_date=None, end_date=None):
        if start_date and end_date:
            return Order.objects.filter(created_at__gte=start_date, created_at__lte=end_date)

        else:
            return Order.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form2'] = FormGetDate()
        return context

    def post(self, request, **kwargs):

        if 'download' in request.POST:
            forms = FormGetDate(request.POST)
            if forms.is_valid():
                qs = self.get_queryset(start_date=forms.cleaned_data['date1'], end_date=forms.cleaned_data['date2'])

            else:
                qs = self.get_queryset()
        elif 'show' in request.POST:
            forms = FormGetDate(request.POST)
            form = ForrmatForm()
            if forms.is_valid():
                qs = self.get_queryset(start_date=forms.cleaned_data['date1'], end_date=forms.cleaned_data['date2'])
                # HomePage.start_date = forms.cleaned_data['date1']
                # HomePage.end_date = forms.cleaned_data['date2']
                return render(request, self.template_name, {"date": qs, "form2": forms, 'form': form})
            else:
                qs = self.get_queryset()

        else:
            qs = self.get_queryset()
        # paginator = Paginator(qs, 2)
        # page_number = request.GET.get("page")
        # page_obj = paginator.get_page(page_number)
        dataset = PostResourse().export(qs)
        format = request.POST.get("format")
        if format == 'xls':
            ds = dataset.xls
        elif format == "csv":
            ds = dataset.csv
        elif format == 'json':
            ds = dataset.json
        else:
            ds = dataset.xls
            format = 'xls'
        response = HttpResponse(ds, content_type=f'{format}')
        response['Content-Disposition'] = f"attachment; filename=orders.{format}"
        return response


class ChartListView(ListView):
    model = CustomerUser
    template_name = "dashbord/chart_list.html"
    context_object_name = 'user_data'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        age_groups = {'0-10': 0, '11-20': 0, '21-30': 0, '31-40': 0, '41+': 0}
        today = date.today()

        for user in context['user_data']:
            if user.birth_day is not None:
                age = today.year - user.birth_day.year - (
                        (today.month, today.day) < (user.birth_day.month, user.birth_day.day))
                if age <= 10:
                    age_groups['0-10'] += 1
                elif age <= 20:
                    age_groups['11-20'] += 1
                elif age <= 30:
                    age_groups['21-30'] += 1
                elif age <= 40:
                    age_groups['31-40'] += 1
                else:
                    age_groups['41+'] += 1
            else:
                age = 0

        context['labels'] = list(age_groups.keys())
        context_data = list(age_groups.values())
        context['data'] = context_data
        return context
