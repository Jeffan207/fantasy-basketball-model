This is my fantasy basketball model. The goal of the model is represent a players overall worth with a simple
number rating. The key benefit of this system is it lets you stack rank your team and give you an idea
who are your best and most importantly, worst, players are. It's pretty simple but I've found it to be very effective in evaluating
the general skill of a player in the category format. This model is not 1:1 with points based scoring systems
used in fantasy. Those systems tend to universally undervalue blocks and steals that are much more
important in category formats.

The model itself is based off of using the average category values for a week-to-week match-up in fantasy
basketball. The average number for each category is divided into the average value for the points category (which
I just used as a simple baseline) to produce a weighted value. What followed was a very straight forward scaling system that values more infrequent categories
like blocks and steals highly and more common categories like rebounds and points less. I trained this number by pulling 
data from my fantasy league from the 2018-2019 season using around ~10 or so weeks of match data. 

Below is the average category values per matchup from my data.

| Category | Average Value | Weighted Value |
|-----|----------|----------|
| FG% | 0.46265  |          |
| FT% | 0.777633 |          |
| 3PM | 52.71667 | 10.92033 |
| REB | 218.15   | 2.638933 |
| AST | 124.7    | 4.616546 |
| STL | 36.28333 | 15.86633 |
| BLK | 24.75    | 23.25993 |
| TO  | 73.81667 | 7.798826 |
| PTS | 575.6833 | 1        |