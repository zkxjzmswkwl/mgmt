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
    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} | {self.name} | Completed -> {self.completed}"


class TaskUpdate(models.Model):
    poster = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    content = MarkdownField(rendered_field="content_rendered", validator=VALIDATOR_STANDARD)
    marked_as_completed = models.BooleanField(default=False)
