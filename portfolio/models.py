# ## Project:
#    - id (primary key)
#    - portfolio_id (foreign key referencing the Portfolio table)
#    - title
#    - description
#    - image_url
#    - created_at
#    - updated_at


from django.db import models
from django.contrib.auth import get_user_model
from skills.models import Skills


class Portfolio(models.Model):
    user_id = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class PortFolioSkill(models.Model):
    portfolio_id = models.ForeignKey(to=Portfolio, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(to=Skills, on_delete=models.CASCADE)
