#HMW-1
#task-1
import pandas as pd

df = pd.DataFrame({
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
    
})


df = df.rename(columns={"First Name":"first_name","Age":"age"})

print(df)

#task-2
import pandas as pd

df = pd.DataFrame({
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
    
})


df = df.head(3)
print(df)

#task-3
import pandas as pd

df = pd.DataFrame({
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
    
})


mean_age=df['Age'].mean()

print(f"Average age: {mean_age}")

#task-4

import pandas as pd

df = pd.DataFrame({
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
    
})

#standard way
selected=df[['City', 'First Name']]

print(selected)

#second way Using loc (best for selecting rows and columns together):

secondway=df.loc[:,['City','First Name']]

print(secondway)

#third way Using filter() method (useful for partial matching or regex):
thirdway=df.filter(items=['City','First Name'])

print(thirdway)

#fourthway using regex
fourthway=df.filter(regex='First Name|City')

print(fourthway)

#Task-5
import pandas as pd

import numpy as np

df = pd.DataFrame({
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
    
})


df['Salary']=np.random.randint(3000,10000,size=len(df))
print(df)

#task-6
import pandas as pd

df = pd.DataFrame({
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
})


print(df.describe(include='all'))

#HMW2
#TASK-1
import pandas as pd

data={'Month':['January','February','March','April'],'Sales':[5000,6000,7500,8000],'Expenses':[3000,3500,4000,4500]}
df=pd.DataFrame(data)

max_sales_and_expenses = df[['Sales','Expenses']].max()

mean_sales_expenses=df[['Sales','Expenses']].mean()

print(df)
#TASK-2
print("\nMaximum Sales:", max_sales_and_expenses['Sales'])
#TASK-3
print("\nMaxium Expenses:", max_sales_and_expenses['Expenses'])
#TASK-4
print("\nAverage of Sales:",mean_sales_expenses['Sales'])
#TASK-5
print("\nAverage of Expenses:",mean_sales_expenses['Expenses'])

#HMW3
#TASK-1
import pandas as pd
data=({
    'Category':['Rent','Utilities','Groceries','Entertainment'],
    'January':[1200, 200, 300, 150],
    'February':[1300, 220, 320, 160],
    'March':[1400, 240, 330, 170],
    'April':[1500, 250, 350, 180]
})

df=pd.DataFrame(data)

expenses=pd.DataFrame(data)
#TASK-2
expenses = expenses.set_index('Category')

max_expenses = expenses.max(axis=1)
#TASK-3
min_expenses = expenses.min(axis=1)
#TASK-4
mean_expenses = expenses.mean(axis=1)

print("📈 Maximum Expense per Category:\n", max_expenses)
print("\n📉 Minimum Expense per Category:\n", min_expenses)
print("\n📊 Average Expense per Category:\n", mean_expenses)
