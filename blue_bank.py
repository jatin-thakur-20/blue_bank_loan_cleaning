# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:51:35 2023

@author: jatin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_json(
    r'C:\Users\jatin\Downloads\Python+Tableau Project\Blue_bank\loan_data_json.json')

data.head()

data.columns
# 'credit policy':- 1 if customer meets the credit underwriting criteria, 0 if the customer does not meet the criteria
# 'installment':- monthly installments inn dollars
# 'log.annual.inc':- natural log of the annual income, we will takr the exponent of this value to get the actual income
# 'dti':- debt to annual income ratio
# 'FICO':- credit score, we can label whether a credit score is good or poor
# 'days.with.cr.line':- no. of days the borrower has had a credit line
# 'revol.bal':- amount unpaid at the end of the credit card billing cycle
# 'revol.util':- %age of credit line used out of the total available
# 'delinq.2yr':- no. of time a borrower had been 30 days past due on a payment in the past two years, this can be used to determine the validity of the borrower
# 'pub':- no. of derogatory public records

data['purpose'].value_counts()

details = data.describe()

data['int.rate'].describe()
data['fico'].describe()
data['dti'].describe()

data.dtypes

data['annual_income'] = np.exp(data['log.annual.inc'])


def ficoscore(score):
    if score >= 300 and score < 400:
        return 'Very Poor'
    elif score >= 400 and score < 600:
        return 'Poor'
    elif score >= 600 and score < 660:
        return 'Fair'
    elif score >= 660 and score < 780:
        return 'Good'
    elif score >= 780:
        return 'Excellent'
    else:
        return 'Unknown'


data['fico.category'] = data['fico'].apply(ficoscore)

data['fico.category'].value_counts()

# df.loc[df[columnname] condition, newcolumnname] = 'value if condition is met'

data.loc[data['int.rate'] > 0.12, 'int.rate.type'] = 'High'
data.loc[data['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

data['fico.category'].value_counts().plot.bar(color='g')
plt.show()

data['purpose'].value_counts().plot.bar(color='r')
plt.show()

plt.scatter(data['annual_income'],data['dti'])
plt.xlabel('Annual Income')
plt.ylabel('Debt to Income ratio')
plt.legend()
plt.show()

data.to_csv('loan_cleaned.csv', index=True)
















