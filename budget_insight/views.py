from django.shortcuts import render, redirect

from budget_insight.models import BudgetInsight, save_budget_data_to_database
from system_management.models import Profile
import pandas as pd

# Create your views here.
def dashboard(request):
    return render(request,'budget_insight/dashboard.html')

def view_all_customers(request):
    if request.method == 'GET':
        customers = Profile.objects.all()
        context = {'customers':customers}
        return render(request, 'budget_insight/all_customers.html', context)
    return render(request,'budget_insight/all_customers.html')

def create_customer(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', False)
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        file = request.FILES.get('file')
        if file:
            file_name = file.name
            if file_name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file_name.endswith('.xls') or file_name.endswith('.xlsx'):
                df = pd.read_excel(file)
                
            customer = Profile.objects.create(date_of_birth=date_of_birth,
                                    first_name=first_name,
                                    last_name=last_name)
            
            save_budget_data_to_database(df, customer)
            return redirect('view_all_customers')
    return render(request, 'budget_insight/all_customers.html')

def view_customer(request, customer_id):
    if request.method == 'GET':
        customer = Profile.objects.get(id=customer_id)
        budget_insight = BudgetInsight.objects.filter(customer_id=customer_id)
        budget_insight_data = pd.DataFrame(budget_insight.values('month', 'income', 'expense'))
        budget_insight_data = budget_insight_data.to_json(orient='records')
        context = {'customer':customer,
                   'budget_insight':budget_insight,
                   'budget_insight_data':budget_insight_data}
        return render(request, 'budget_insight/view_customer.html', context)
    return render(request, 'budget_insight/view_customer.html')