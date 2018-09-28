"""Forms related to sub project detail """
from typing import List, Tuple

from django import forms
from django.db.models import Sum

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, MultiField
from django.template.defaultfilters import slugify
from django.utils.datetime_safe import datetime
from django.utils.formats import get_format
from mptt import models
from django.utils.html import mark_safe

from .abstract import BaseHorizontalForm
from tms.models import ProjectDetails
from tms.models import Projecttype
from tms.models import Project_status
from tms.models import Client
from tms.constants import PROJECT_STATUS, PROJECT_LIST
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import ModelChoiceField
# from tms.models import Projecttype,Client_name
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, PrependedAppendedText
from bootstrap_datepicker_plus import DatePickerInput


class Subprojecttimesheetform(BaseHorizontalForm):
    """Form for DailyTimesheet"""

    project_type = forms.ChoiceField(choices=PROJECT_LIST, label="Project type", required=True)
    client = forms.ModelChoiceField(queryset=Client.objects.filter(client_type="client").order_by('id'),
                                    label="Client Name", required=True,
                                    empty_label="-- Select a Client --")
    enduser = forms.ModelChoiceField(queryset=Client.objects.filter(client_type='end_user').order_by('id'),
                                     label="End User Name", required=True,
                                     empty_label="-- Select a End User --")
    project_status = forms.ModelChoiceField(queryset=Project_status.objects.all().order_by('id'),
                                            label="Project status",
                                            required=True, empty_label="-- Select a Status --")

    project_name = forms.CharField(label="Project Name", required=True, max_length=1000)

    project_startdate = forms.DateField(
        label="Project startdate",

        input_formats=("%d-%m-%Y",),

        widget=forms.DateInput(
            attrs=
            {
                'class': 'datepicker',
                'id': "fromdate",
                'format': "%d-%m-%Y",
            }))
    project_enddate = forms.DateField(
        input_formats=("%d-%m-%Y",),
        label="Project enddate",
        widget=forms.DateInput(
            attrs=
            {
                'class': 'datepicker',
                'id': "todate",
                'format': "%d-%m-%Y",

            }))

    test = forms.DateField(
        widget=DatePickerInput(format='%m/%d/%Y')
    )

    project_description = forms.CharField(
        label="Description",
        max_length=2000,
        required=False,
        widget=forms.Textarea(
            attrs={'rows': 4, 'cols': 40}))

    subproject_code = forms.CharField(label="Sub project code", required=True)
    subproject_name = forms.CharField(label="Sub project name", required=True)

    def __init__(self, *args, **kwargs):
        super(Subprojecttimesheetform, self).__init__(*args, **kwargs)
        self.fields['client'].label_from_instance = lambda obj: "%s" % obj.client_name
        self.fields['enduser'].label_from_instance = lambda obj: "%s" % obj.client_name
        self.fields['project_status'].label_from_instance = lambda obj: "%s" % obj.project_status
        self.fields['parent'].label_from_instance = lambda obj: "%s" % obj

        self.helper.layout = Layout(
            Div(
                Field('test', ),
                Field('project_type', ),
                Field('project_code', ),
                Field('project_name', ),

                'parent',
                'subproject_code',
                'subproject_name',
                'client',
                'enduser',
                'project_startdate',
                'project_enddate',
                'project_status',
                'project_description',

                css_class='item form-group'
            ),

            # Field('project_code' ),
            # Field('taskdescription', rows="3", css_class='control-label col-md-3 col-sm-3 col-xs-12'),
            # FormActions(
            #     Submit('save', 'Submit'),
            #     Button('cancel', 'Back', css_class="btn btn-danger")
            # )

        )

    class Meta:
        """Meta Attributes"""
        model = ProjectDetails
        fields = (
            'project_type', 'project_code', 'project_name', 'project_description', 'client', 'enduser',
            'project_startdate', 'project_enddate', 'project_status', 'parent',)
