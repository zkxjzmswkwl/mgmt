from django.db import models
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
from member.models import Member

PRIORITY_CHOICES = (
    ("Needed yesterday", u"Needed yesterday"),
    ("Highest", u"Highest"),
    ("Important", u"Important"),
    ("Medium", u"Medium"),
    ("Low", u"Low")
)


class Task(models.Model):
    name = models.CharField(max_length=72)
    description = MarkdownField(rendered_field="description_rendered", validator=VALIDATOR_STANDARD)
    description_rendered = RenderedMarkdownField()
    assigned_to = models.ForeignKey(Member, related_name="member", on_delete=models.CASCADE)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=28)
    needed_by = models.DateTimeField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
