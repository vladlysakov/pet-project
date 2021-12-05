from django.db.models import Model, UUIDField, DateTimeField


class AbstractBaseModel(Model):
    uuid = UUIDField(primary_key=True, editable=False, unique=True)
    created_at = DateTimeField('Created at', auto_now_add=True)
    updated_at = DateTimeField('Updated at', auto_now=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.uuid}>'
