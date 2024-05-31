from django.db import models

from system_management.models import Profile

def save_budget_data_to_database(df, customer):
    for index, row in df.iterrows():
        month = row['Month']
        income = row['Income']
        expense = row['Expenses']
        
        # Create a new BudgetInsight object and save it to the database
        budget_insight = BudgetInsight(
            customer=customer,
            income=income,
            expense=expense,
            month=month
        )
        budget_insight.save()

# Create your models here.
class BudgetInsight(models.Model):
    """
    Model representing a budget insight.
    """

    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    income = models.FloatField()
    expense = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    month = models.CharField(max_length=20, null=True)