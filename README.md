OUStats.csv is a file including every pokemon, by their name in pokemon showdown, in the pokedex as of 2024 and their base stats.

  I am interested in competetive singles pokemon, the most popular tier of this format is OU, or overused which include the strongest pokemon but not including 
the oppressively powerful ones including many legendaries.

  On pokemon showdown, an online pokemon battle simulator, they release the percent usage of the most 
popular pokemons every month. 

  So I imported the data from September to December, as those are the months containign the data from the Teal Mask, into a couple of CSV file and then merged them on
  Name with another csv containing the base stats of each of every pokemon.
  
  This is when I realized that many of the names are not formatted the same, so I had to instead focus on converting them all to the same format as used on 
pokemon showdown.

  For example Blastoise and Mega Blastoise will be listed as having the same name despite having different base stats, to fix this I would add '-Mega' to any 
pokemon that contains 'Mega' in its form column. I then copied this process for 'Galar' 'Hisui' and 'Alolan' forms. 

  I also queried for all pokemon containing 'Form' in its form column and then added the preceding portion of the string to the Name value. 
For example: there are 2 Blastoises in the name column, however one has an empty form value for the base form, while the other has 'Mega Blastoise' in its form column.
The 2nd one will have its name changed to 'Blastoise-Mega'

In the future I will plan on including all possible abiliites and what tier they are placed in

I wanted to soften the barrier to entry to competetive pokemon and help those interested in learning more about it. Hope you enjoyed!
