from glob import glob
import pandas as pd

def get_hour(x):
    return f"{x[0:2]}:{x[2:4]}"

def get_timestamp(data, hora):
    return f"{data} {hora}"

def get_rainy_days(data_path,
                   months_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   threshold=50):
    
    csv_list = sorted(glob(f'{data_path}/*.csv'))

    date_list = []

    for csv_file in csv_list:

        df = pd.read_csv(csv_file,
                        encoding='iso-8859-1',
                        decimal=',',
                        delimiter=';',
                        skiprows=8,
                        usecols=['Data', 'Hora UTC', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'],
                        parse_dates=['Data'])
        
        df['Data'] = df['Data'].astype(str)
        df.rename(columns={"PRECIPITAÇÃO TOTAL, HORÁRIO (mm)": "precipitacao"}, inplace=True)

        df['Hora'] = df['Hora UTC'].apply(get_hour)

        df['timestamp'] = df[['Data', 'Hora']].apply(lambda x: get_timestamp(*x), axis=1)
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        # Group by day and sum the precipitation
        df_result = (df.groupby(pd.Grouper(key='timestamp', axis=0, freq='D'))
                    .sum(numeric_only=True)
                    .sort_values(by=['precipitacao'], ascending=False)
                    .reset_index()
                    .copy())
        
        # Filter by precipitaton threshold
        filter_ppt = (df_result['precipitacao']>threshold)
        df_result = df_result[filter_ppt]

        # Filter by list of months
        df_result = df_result[df_result['timestamp']
                            .dt.month
                            .isin(months_list)
                            .copy()]

        for i in range(len(df_result.index)):
            date_list.append(str(df_result['timestamp'].iloc[i]))

    date_list = sorted(list( dict.fromkeys(date_list) )) # remove duplicates and sorted
    date_list = [time[0:10] for time in date_list] # remove 00:00:00

    return date_list