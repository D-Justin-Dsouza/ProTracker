import matplotlib.pyplot as plt
import pandas as pd

def pie_chart(df):
    category_data=df.groupby('Category')['Hours'].sum()
    fig, ax = plt.subplots()
    ax.pie(category_data, labels=category_data.index, autopct='%1.1f%%', startangle=100)
    ax.set_title('Time Spent by Category')
    return fig

def bar_chart(df):
    daily_data = df.groupby('Date')['Hours'].sum()
    fig, ax= plt.subplots()
    ax.bar(daily_data.index, daily_data.values, color='skyblue')
    ax.set_xlabel('Date')
    ax.set_ylabel('Hours Spent')
    ax.set_title('Daily Time Spent on Tasks')
    plt.xticks(rotation=45)
    return fig

def score_line_chart(df):
    daily_scores = df.groupby('Date')['Score'].sum().sort_index()
    fig, ax = plt.subplots()
    ax.plot(daily_scores.index, daily_scores.values, marker='o', color='green')
    ax.set_xlabel('Date')
    ax.set_ylabel('Productivity Score')
    ax.set_title('Daily Productivity Score')
    plt.xticks(rotation=45)
    return fig
