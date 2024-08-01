from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from users.models import Member
from .forms import MemberForm

def index(request):
    return render(request,'index.html')
def about(request):
    all_members = Member.objects.all
    return render(request, 'about.html', {'all': all_members})

def join(request):
    if request.method == "POST":
    # if its a post request (comes from the join.html) its doing something with the form,
    # if its something else we just return get request for the join html
        form = MemberForm(request.POST )
        if form.is_valid():
            form.save()
    else:
        form = MemberForm()
    return render(request,'join.html', )


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()


