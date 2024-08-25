import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Load the data
df = pd.read_csv('medical_examination.csv')

# 2: Calculate BMI and add 'overweight' column
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3: Normalize cholesterol and gluc
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5: Melt data
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # 6: Group data by cardio and count
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat.columns = ['cardio', 'variable', 'value', 'total']
    
    # 7: Draw the catplot
    fig = sns.catplot(x="variable", y="total", hue="value", col="cardio", kind="bar", data=df_cat).fig
    
    # 8: Save plot to file and return figure
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    # 11: Clean data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # 12: Select specific columns
    df_heat = df_heat[['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']]
    
    # 13: Calculate the correlation matrix
    corr = df_heat.corr()
    
    # 14: Generate mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # 15: Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # 16: Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='coolwarm', ax=ax, cbar_kws={'shrink': .5})
    
    # 17: Save plot to file and return figure
    fig.savefig('heatmap.png')
    return fig
