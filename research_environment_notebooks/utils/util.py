import numpy as np
import pandas as pd


def date_variable_extraction(df, var):
    df = df.copy()
    df[var] = pd.to_datetime(df[var])
    df['dt_day'] = df[var].dt.day  # day from 1-31
    df['dt_week'] = df[var].dt.week  # week of year from 1 to 52
    df['dt_month'] = df[var].dt.month  # month from date - 1 to 12
    df['dt_quater'] = df[var].dt.quarter  # quater from date - 1 to 4
    df['dt_dayofweek'] = df[var].dt.day_name()  # day name from Sunday - Saturday
    df['dt_is_weekend'] = np.where(df['dt_dayofweek'].isin(['Sunday', 'Saturday']), 1, 0)  # if weekend from date 0 & 1

    dt_vars = [var for var in df.columns if 'dt' in var]
    df[dt_vars] = df[dt_vars].astype(object)
    return df

