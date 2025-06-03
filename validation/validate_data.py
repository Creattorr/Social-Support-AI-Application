def validate_consistency(app_df, credit_df):
    inconsistencies = []
    for _, row in app_df.iterrows():
        credit_row = credit_df[credit_df['Name'] == row['Name']]
        if credit_row.empty:
            inconsistencies.append((row['Name'], 'Missing credit report'))
    return inconsistencies
