from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Positive
from .forms import PositiveForm
from django.core.paginator import EmptyPage, Paginator
from django.contrib import messages


class PaginatorSafe(Paginator):
    """
    Prevent fan(s) to type the wrong page
    in the adressbar other then those existing
    """
    def validate_number(self, number):
        try:
            return super(PaginatorSafe, self).validate_number(number)
        except EmptyPage:
            if number > 1:
                return self.num_pages
            else:
                raise


class PositiveListView(generic.ListView):
    """
    Defines how the stories are listed/shown on the
    home page
    """
    model = Positive
    queryset = Positive.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginator_class = PaginatorSafe
    paginate_by = 6


class PositiveDetail(View):
    """
    Class for a single story view
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Creates the view for a single specific story
        """
        queryset = Positive.objects.filter(status=1)
        positive = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "positive_detail.html",
            {
                "positive": positive,
            },
        )


@login_required
def edit_positive(request, slug):
    """
    View for edit story
    """
    positive = get_object_or_404(Positive, slug=slug)
    if positive.author == request.user:
        positive_form = PositiveForm(request.POST or None, instance=positive)
        context = {
            "positive_form": positive_form,
            "positive": positive
        }
        if request.method == "POST":
            positive_form = PositiveForm(
                request.POST, request.FILES, instance=positive)
            if positive_form.is_valid():
                positive = positive_form.save(commit=False)
                positive.author = request.user
                positive.save()
                messages.success(request, (
                    "Story has been edited successfully."))
                return redirect('home')
        else:
            positive_form = PositiveForm(instance=positive)
        return render(request, "edit_positive.html", context)
    else:
        raise PermissionDenied()
    return redirect('home')


@login_required
def add_positive(request):
    """
    View for add story
    """
    positive_form = PositiveForm(request.POST or None, request.FILES or None)
    context = {
        'positive_form': positive_form,
    }

    if request.method == "POST":
        positive_form = PositiveForm(request.POST, request.FILES)
        print("hola123")
        if positive_form.is_valid():
            positive_form = positive_form.save(commit=False)
            positive_form.author = request.user
            positive_form.status = 1
            positive_form.save()
            messages.success(request, (
                    "Story has been added successfully."))
            return redirect('home')
    else:
        positive_form = PositiveForm()
    return render(request, "add_positive", context)


@login_required
def delete_positive(request, slug):
    """
    View for delete story
    """
    positive = Positive.objects.get(slug=slug)
    if positive.author == request.user:
        positive.delete()
    else:
        raise PermissionDenied()
    messages.success(request, (
                    "Story has been deleted successfully."))
    return redirect('home')
