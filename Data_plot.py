#The line plot is very random,lets sort the feature and plot it
df_sorted=df.sort_values(by='Total_money_spend',ascending=True)
x=df_sorted['Total_money_spend'].head(500)
print(x.head(10))
y=df_sorted['Total_money_spend_for_each_customer'].head(500)
plt.plot(x,y)
plt.xlabel('Total_money_spend')
plt.ylabel('Total_money_spend_for_each_customer')
plt.title('Total_money_spend vs Total_money_spend_for_each_customer')
plt.show()

# Plotting a smaller subset to clearly print the y-values using plt.text
plt.figure(figsize=(12, 6))

# Take the first 10 sorted records for a clean visualization
x_subset = df_sorted['Total_money_spend'].head(10).tolist()
y_subset = df_sorted['Total_money_spend_for_each_customer'].head(10).tolist()
customer_subset = df_sorted['customer_id'].head(10).tolist()

# Plot the line and points
plt.plot(x_subset, y_subset, marker='o', linestyle='-', color='purple', label='Service Cost')

# Loop through each point and annotate its y-value
for idx, (xi, yi) in enumerate(zip(x_subset, y_subset)):
    plt.text(
        xi,
        yi + 5,                  # Position the text slightly above the point
        f'${yi:.2f}',           # Format the text with two decimal places
        ha='center',
        va='bottom',
        fontsize=9,
        fontweight='semibold',
        color='darkmagenta'
    )

plt.xlabel('Total Money Spend ($)')
plt.ylabel('Total Money Spend For Each Customer ($)')
plt.title('Total Money Spend vs Cost to Serve (First 10 Customers)')
plt.ylim(min(y_subset) - 10, max(y_subset) + 30) # Adjust limit to fit text labels
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

x_bar = df['customer_id'].head(5)
y_bar = df['Total_money_spend'].head(5)

plt.figure(figsize=(10, 6))
bars = plt.bar(x_bar, y_bar, label='employee_expenditure', color='green')

# Adding values on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 10, f'${yval}', ha='center', va='bottom', fontweight='bold')

plt.xlabel('Customer ID')
plt.ylabel('Total Money Spent')
plt.title('Total Money Spent by Top 5 Customers')
plt.ylim(0, max(y_bar) + 100)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()


# Correct histogram to display the distribution of Total Money Spent by customers
plt.figure(figsize=(10, 6))
plt.hist(df_sorted['Total_money_spend'].head(2000), bins=10, color='skyblue', edgecolor='black', rwidth=0.85)

plt.xlabel('Total Money Spend ($)')
plt.ylabel('Frequency (Customer Count)')
plt.title('Distribution of Total Money Spend (First 2000 Customers)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


import matplotlib.pyplot as plt

plt.figure(figsize=(12, 7))

# plt.hist returns: counts (heights), bins (boundaries), and patches (the bar shapes)
counts, bins, patches = plt.hist(
    df_sorted['Total_money_spend'].head(2000), 
    bins=10, 
    color='skyblue', 
    edgecolor='black', 
    rwidth=0.85
)
print("counts",counts)
print("bins",bins)
print("patches",patches)
# Loop through each patch (bar) to place the text label
for patch in patches:
    # Get the height (count) of the bar
    print("patch",patch)
    height = patch.get_height()
    
    # Only display the label if the bar has a height greater than 0
    if height > 0:
        # Calculate X position at the center of the bar
        x_pos = patch.get_x() + patch.get_width() / 2
        # Place text slightly above the top of the bar
        y_pos = height + 5 
        
        plt.text(
            x_pos, 
            y_pos, 
            f'{int(height)}', 
            ha='center', 
            va='bottom', 
            fontsize=10, 
            color='darkblue', 
            fontweight='bold'
        )

plt.xlabel('Total Money Spend ($)')
plt.ylabel('Frequency (Customer Count)')
plt.title('Distribution of Total Money Spend with Bin Value Labels')
# Adjust Y-axis limit slightly so labels don't get cut off at the top
plt.ylim(0, max(counts)+100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


import matplotlib.pyplot as plt

plt.figure(figsize=(12, 7))

# plt.hist returns: counts (heights), bins (boundaries), and patches (the bar shapes)
counts, bins, patches = plt.hist(
    df_sorted['Total_money_spend'].iloc[50000:60000],
    bins=10,
    color='skyblue',
    edgecolor='black',
    rwidth=0.85
)
print("counts",counts)
print("bins",bins)
print("patches",patches)
# Loop through each patch (bar) to place the text label
for patch in patches:
    # Get the height (count) of the bar
    print("patch",patch)
    height = patch.get_height()

    # Only display the label if the bar has a height greater than 0
    if height > 0:
        # Calculate X position at the center of the bar
        x_pos = patch.get_x() + patch.get_width() / 2
        # Place text slightly above the top of the bar
        y_pos = height + 5

        plt.text(
            x_pos,
            y_pos,
            f'{int(height)}',
            ha='center',
            va='bottom',
            fontsize=10,
            color='darkblue',
            fontweight='bold'
        )

plt.xlabel('Total Money Spend ($)')
plt.ylabel('Frequency (Customer Count)')
plt.title('Distribution of Total Money Spend with Bin Value Labels')
# Adjust Y-axis limit slightly so labels don't get cut off at the top
plt.ylim(0, max(counts)+100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


#pie chart
import matplotlib.pyplot as plt

# Compare the profit earned from a few customers
df_sorted = df.sort_values(by='Total_money_spend', ascending=True)
df_pie_shared = df_sorted.iloc[115:120]

# Get the profit values
shared = df_pie_shared['Profit_earned_from_customer'].tolist()
customer_id = df_pie_shared['customer_id'].tolist()

print("Values:", shared)
print("Labels:", customer_id)

# Provide at least 5 colors for 5 slices
colors_list = ['magenta', 'cyan', 'brown', 'gold', 'violet']

plt.figure(figsize=(8, 8))
# Fixed: Pass customer_id explicitly as a keyword argument (labels=customer_id)
plt.pie(shared, labels=customer_id, colors=colors_list, startangle=0, shadow=True,explode=(0.2,0.2,0.2,0.2,0.2), autopct='%.2f%%')
plt.legend(loc='upper right')
plt.title('Profit earned from few customers')
plt.show()


# Seaborn library to plot distributions
import matplotlib.pyplot as plt

import seaborn as sns

# Plot distribution of Total Money Spend
sns.displot(data=df, x='Total_money_spend', kde=True, color='skyblue')
plt.title('Distribution of Total Money Spend')
plt.show()

# Plot distribution of Profit Earned from Customers
sns.displot(data=df, x='Profit_earned_from_customer', kde=True, color='teal')
plt.title('Distribution of Profit Earned')
plt.show()


# Plot distribution of Profit Earned with value labels using plt.text
import matplotlib.pyplot as plt
import seaborn as sns

# Fixed: Reverted kind to 'hist' (default) so that 'bins' is valid and patches exist to label
g = sns.displot(data=df, x='Profit_earned_from_customer', bins=10, kind='hist', color='teal', height=6, aspect=1.5)

# Access the underlying matplotlib axes
ax = g.ax

# Loop through each bar patch to annotate its height on top
for patch in ax.patches:
    height = patch.get_height()
    if height > 0:  # Only annotate bars that have a height
        # Find center of the bar on the X-axis
        x_pos = patch.get_x() + patch.get_width() / 2
        # Position the text slightly above the top of the bar
        y_pos = height + (df.shape[0] * 0.0002)
        
        ax.text(
            x_pos,
            y_pos,
            f'{int(height)}',
            ha='center',
            va='bottom',
            fontsize=10,
            fontweight='bold',
            color='darkslategrey'
        )

plt.title('Profit Distribution with Bar Value Labels')
plt.show()



fg = sns.countplot(data=df, x='churn', palette='pastel')
axis = fg  # Fix: fg is already the Axes object, no need for .ax
for patch in axis.patches:
    height = patch.get_height()
    if height > 0:
        x_pos = patch.get_x() + patch.get_width() / 2
        y_pos = height + (df.shape[0] * 0.0002)
        axis.text(
            x_pos,
            y_pos,
            f'{int(height)}',
            ha='center',
            va='bottom',
            fontsize=10,
            fontweight='bold',
            color='darkslategrey'
        )
plt.title('Distribution of Churn')
plt.show()


sns.boxplot(data=df, x='churn', y='Total_money_spend', palette='pastel')
plt.title('Total Money Spend vs Churn')
plt.show()
#
