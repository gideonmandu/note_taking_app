from tortoise import fields, models


class AbstractBase(models.Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    
    class Meta:
        abstract = True
    

class Users(AbstractBase):
    username = fields.CharField(max_length=20, unique=True)
    full_name = fields.CharField(max_length=50)
    password = fields.CharField(max_length=255)
    note: fields.ForeignKeyRelation['Notes']
    
    class PydanticMeta:
        exclude: ("created_at", "modified_at")


class Notes(AbstractBase):
    title = fields.CharField(max_length=225)
    content = fields.TextField()
    author: fields.ForeignKeyRelation["Users"] = fields.ForeignKeyField(
        "models.Users", related_name="note"
    )

    def __str__(self):
        return f"{self.title}, {self.author_id} on {self.created_at}"