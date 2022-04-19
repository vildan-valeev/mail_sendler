from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    class Meta:
        abstract = True


class Follower(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    b_date = models.DateTimeField()
    email = models.EmailField()
    group = models.ForeignKey('FollowerGroup', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} | {self.first_name} {self.last_name}'


class FollowerGroup(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id} | {self.name}'


class HtmlTemplate(BaseModel):
    name = models.CharField(max_length=100)
    html_template = models.FileField(upload_to='html_templates')

    def __str__(self):
        return f'{self.id} | {self.name}'


class EmailSendler(BaseModel):
    from_email = models.EmailField()
    subject = models.CharField(max_length=78)
    text = models.TextField(max_length=3000)
    follower_group = models.ForeignKey(FollowerGroup, on_delete=models.PROTECT, blank=True, null=True)
    html_template = models.ForeignKey(HtmlTemplate, on_delete=models.PROTECT, blank=True, null=True,
                                      related_name='sendlers')
    delayed = models.DateTimeField(help_text='Choose time when need to send emails,', blank=True, null=True)

    def __str__(self):
        return f'{self.id} | {self.subject}'
