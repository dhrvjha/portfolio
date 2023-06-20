# ## Domain:
#    - id (primary key)
#    - user_id (foreign key referencing the User table)
#    - portfolio_id
#    - domain_name (unique)
#    - created_at


from django.db import models
from django.contrib.auth import get_user_model

from portfolio.models import Portfolio


class Domain(models.Model):
    user_id = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    portfolio_id = models.ForeignKey(to=Portfolio, on_delete=models.DO_NOTHING)
    name = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
