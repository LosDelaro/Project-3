# Project-3
Project 3
Analysis Summary:
Data cleaning – the data was already in decent useable shape but after looking at the two spreadsheets
we were able to determine that the second spreadsheet was a duplicate with less info in it so we
dropped it. Turning our attention to the main file we dropped 4 columns, reformatted another column
and renamed one as well.
After the data was cleaned, we converted it to both a json and sqlite for further exploration. We made a
few graphics in a jupyter notebook to give us ideas for our visualizations needed in javascript. Which
helped us retune some of our research questions. After doing a general overview we took a deep dive
into the data utilizing ydata_profiling. This gave us an interactive way to look at the data quickly, looking
for correlations and finding clues on topics to investigate. We also took steps to try and calculate the
distance that Anthony Bourdain traveled while filming the show.
Analysis Results:
1. Looking at Anothony Bourdain’s longer running shows, No Reservations and Parts Unknown, we
found some conflicting information. In Parts Unknown the first two season and the last two
seasons had more episodes per seasons than the middle seasons; however, in No Reservations
the seasons had the opposite where the first season had one of the smallest number of episodes
while the middle seasons had many more and sometimes doubling the count for example
season 1 had 21 episodes but season 4 had 48 episodes. As the show ran on the later seasons
began to decline in the number of episodes as well. A Cook’s Tour only had two seasons but
season 1 had 10 more episodes than season 2. Finally, The Layover only had 2 seasons but both
seasons only had 10 episodes. Thus, we were unable to reach a discernable pattern for our
hypothesis which was that as the show goes on longer seasons would have more episodes as the
show gained popularity.
2. Anthony Bourdain traveled all over the world but lived in New York City. After looking at the
regions he visited the most we came to find out that the area most visited by Anthony Bourdain
was in North America but more specifically the United States.
3. With the limited information that we had we were only able to determine the minimum distance
that he traveled, meaning if he started in New York City and just traveled to each of his
destinations in order, came out to be 2,772,900.91 Kilometers which is 1,723,000.74 Miles.
4. Anthony Bourdain’s top show was No Reservations coming in at 275 episodes running just over 7
years.
The Process:
1. We wrote some code to create a donut chart that broke Anthony Bourdain’s shows down by
season and counted each episode per season. And in javascript we were able to make it
interactive allowing you to look at the breakdown of each show when selected

2. To get this answer we created a bar chart that ran through our data and calculated the number
of times that Anthony Bourdain visited a Region over every show.

To take a closer look for trends we then broke it down by show:

3. When calculating distance traveled on a sphere, which the earth is, you must take into
consideration the curvature of the sphere. If you do not take the Earths curvature into
consideration you would be simply calculating the Euclidean distance being the shortest path
between two points, which would mean the number would be smaller. We calculated his
distance travel by utilizing the Great Circle formula

4. Running with the theory that the better a show performs the longer the show lasts, we
calculated which show had the most episodes and ran for the longest time by utilizing air dates
of each episode we concluded that No Reservations was Anthony Bourdain’s top show.

Limitations:
We would have really liked to have been able to use food data. Unfortunately, our dataset did not
include any specific dish references. The only place our team was able to find such information
would have required a great deal of web scraping, which would have taken more time than we had
to complete this project. Also, in terms of the travel distances, our calculations represent a
cumulative path between unique locations; whereas, in reality, he could have traveled back to his
home city of New York between some, or all, of his trips, amassing a great deal more overall miles
traveled.
Future Work:
It would be interesting to acquire food data for all his various travels, and to be able to include that
data in our mapping. We could also try to hunt down additional data about his actual travel paths to
produce more accurate mileage calculations. 
