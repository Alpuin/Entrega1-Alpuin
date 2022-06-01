from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from app.models import Staff, Project, Product
from app.forms import StaffForm, ProjectForm, ProductForm


def index(request):
    return render(request, "app/index.html")


def staffs(request):
    return render(request, "app/staffs.html")


def projects(request):
    return render(request, "app/projects.html")


def products(request):
    return render(request, "app/products.html")


def staffs_forms(request):
    if request.method == 'POST':
        staff_form = StaffForm(request.POST)
        if staff_form.is_valid():
            data = staff_form.cleaned_data
            staff = Staff(
                name=data['name'],
                last_name=data['last_name'],
                position=data['position'],
                rank=data['rank'],
                since=data['since'],
                email=data['email']
            )
            staff.save()

            staffs = Staff.objects.all()
            context_dict = {
                'staffs': staffs
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app/staffs.html"
            )

    staff_form = StaffForm(request.POST)
    context_dict = {
        'staff_form': staff_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app/staff_forms.html'
    )


def projects_forms(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            data = project_form.cleaned_data
            project = Project(
                code=data['code'],
                title=data['title'],
                start=data['start'],
                state=data['state']
            )
            project.save()

            projects = Project.objects.all()
            context_dict = {
                'projects': projects
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app/projects.html"
            )

    project_form = ProjectForm(request.POST)
    context_dict = {
        'project_form': project_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app/project_forms.html'
    )


def products_forms(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            data = product_form.cleaned_data
            product = Product(
                serial=data['serial'],
                product_name=data['product_name'],
                availability=data['availability']
            )
            product.save()

            products = Product.objects.all()
            context_dict = {
                'products': products
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app/products.html"
            )

    product_form = ProductForm(request.POST)
    context_dict = {
        'product_form': product_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app/product_forms.html'
    )


    # def search(request):