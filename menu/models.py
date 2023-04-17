from django.db import models
from django.urls import reverse


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    id_parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=2047, blank=True, null=True)
    named_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        elif self.url:
            return self.url
        else:
            return ""

    def get_urls(self):
        children = self.children()
        if not children:
            return [self.get_url()]
        else:
            result = []
            for child in children:
                result += child.get_urls()
            result.append(self.get_url())
            return result

    def children(self):
        return self.menuitem_set.all()

    def get_elder_ids(self):
        if self.id_parent:
            return self.id_parent.get_elder_ids() + [self.id_parent.id]
        else:
            return []
