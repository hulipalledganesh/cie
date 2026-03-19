# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# PART 1: Pivot Table
# -------------------------------

data = {
    'product_Name': ['ac', 'shirt', 'table', 'tava'],
    'category': ['electronics', 'clothing', 'home', 'kitchen'],
    'price': [50000, 2000, 10000, 800],
    'quantity_sold': [3, 8, 6, 10]
}

df1 = pd.DataFrame(data)

pivot_table = pd.pivot_table(
    df1,
    values=['quantity_sold', 'price'],
    aggfunc=['sum', 'mean'],
    index='category'
)

print("Pivot Table:\n", pivot_table)


# -------------------------------
# PART 2: Load Dataset
# -------------------------------

df = pd.read_csv('/content/mtcars (1).csv')


# -------------------------------
# PART 3: Histogram
# -------------------------------

plt.figure(figsize=(8, 6))
plt.hist(df['mpg'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of MPG')
plt.xlabel('MPG')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# -------------------------------
# PART 4: Scatter Plot
# -------------------------------

plt.figure(figsize=(8, 6))
plt.scatter(df['wt'], df['mpg'], color='green')
plt.title('Weight vs MPG')
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.grid(True)
plt.show()


# -------------------------------
# PART 5: Bar Chart
# -------------------------------

transmission_counts = df['am'].value_counts()

plt.figure(figsize=(8, 6))
transmission_counts.plot(kind='bar', color='orange')
plt.title('Transmission Type Count')
plt.xlabel('0 = Automatic, 1 = Manual')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()


# -------------------------------
# PART 6: Box Plot (Vertical)
# -------------------------------

plt.figure(figsize=(8, 6))
plt.boxplot(df['mpg'])
plt.title('Boxplot of MPG')
plt.ylabel('MPG')
plt.show()


# -------------------------------
# PART 7: Box Plot (Horizontal)
# -------------------------------

plt.figure(figsize=(8, 6))
plt.boxplot(df['mpg'], vert=False)
plt.title('Horizontal Boxplot of MPG')
plt.xlabel('MPG')
plt.grid(axis='x')
plt.show()
