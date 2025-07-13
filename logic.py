category_weights={
    'Study': 3.5,
    'Work':3,
    'Gym':2,
    'Social':1.5,
    'Other':1
}
def calculate_score(category, hours):
    weight = category_weights.get(category, 1)
    return round(weight * hours, 2)
def apply_score(df):
    df['Score']=df.apply(lambda row: calculate_score(row['Category'], row['Hours']), axis=1)
    return df