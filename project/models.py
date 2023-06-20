# ## Project:
#    - id (primary key)
#    - portfolio_id (foreign key referencing the Portfolio table)
#    - title
#    - description
#    - created_at
#    - updated_at

# ## Images:
#    - id (primary key)
#    - project_id (foreign key referencing the project table)
#    - url (URL field to store link of s3 object)
#    - decription (text field)


from django.db import models
from portfolio.models import Portfolio
from skills.models import Skills

class Project(models.Model):
    project_owner_id = models.ForeignKey(to=Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Images(models.Model):
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    url = models.URLField()
    decription = models.TextField()


class ProjectSkill(models.Model):
    project_id = models.ForeignKey(to=Project, on_delete=models.DO_NOTHING)
    skill_id = models.ForeignKey(to=Skills, on_delete=models.DO_NOTHING)
