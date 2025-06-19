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

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data)
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
