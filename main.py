import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

def make_usable(month_data):
    df = pd.read_csv(month_data)
    df = df.merge(stats, left_on ='Pokemon', right_on = 'Name', how = 'left')
    
    df_int = df.assign(Rank = (df.get('Rank').apply(int)))     #turns values in 'Rank' Column to integers
    df_int['Percent'] = df_int['Percent'].str.replace('%', '')  # removes the percentage symbol so the values can be converted to floats
    ox_float = df_int.assign(Percent = (df_int.get('Percent').apply(float)))#turns values in 'Percent' Column to floats
    return ox_float

    
sep = '/Users/chiragamatya/Desktop/OU Stats/SV_OU_Usage_DLC1_CSV_Stats_September.csv'
oct = '/Users/chiragamatya/Desktop/OU Stats/SV_OU_Usage_DLC1_CSV_Stats_October.csv'
nov = '/Users/chiragamatya/Desktop/OU Stats/SV_OU_Usage_DLC1_CSV_Stats_November.csv'
Pokedex_stats = '/Users/chiragamatya/Desktop/OU Stats/Pokemon.csv'
stats = pd.read_csv(Pokedex_stats)
stats['Form'] = stats['Form'].fillna('')

stats['Name'] += stats['Form'].str.extract(r'(.+?) Forme', expand=False).fillna('')
stats['Name'] += stats['Form'].str.extract(r'(.+?) Form', expand=False).fillna('')

stats.loc[stats['Form'].str.contains('Galar'), 'Name'] += '-Galar'
stats.loc[stats['Form'].str.contains('Alolan'), 'Name'] += '-Alola'
stats.loc[stats['Form'].str.contains('Paldean'), 'Name'] += '-Paldea'
stats.loc[stats['Form'].str.contains('Hisui'), 'Name'] += '-Hisui'
stats.loc[stats['Form'].str.contains('Mega'), 'Name'] += '-Mega'



September = make_usable(sep)
October = make_usable(oct)
November = make_usable(nov)

stats.to_csv('OUStats.csv', index=False)

def show_plot(month,custom_color): 
    month10 = month.take(np.arange(10)).set_index('Pokemon')
    colors = plt.cm.get_cmap(custom_color)(np.linspace(.9, .5, len(month10)))
    month10.plot(kind = 'bar',y = 'Percent', color=colors)
    plt.title('Top 10 Pokemon of the Month')
    plt.xlabel('Pokemon')
    plt.ylabel('Percentage')
    plt.xticks(rotation=330)  # certain names are long and overlap, tilt helps it fit
    plt.show()                    
    return 0
#show_plot(September,'Reds')#pick a month
#print((October.get('Generation').iloc[0]))