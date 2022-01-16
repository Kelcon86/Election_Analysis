# Election_Analysis

## Project Overview
Using Python we evaluated election data for three counties in Colorado to do the following:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.63.2

## Election-Audit Results
![Election_Results](https://user-images.githubusercontent.com/60076980/149666719-d29cb549-0453-48f2-876e-a93391be22e4.png)

The analysis of the election show that:

- There were 369,711 votes cast in the election.

- The votes by county were:
  - Jefferson: 38,855 votes (10.5%)
  -  Denver: 306,055 (82.8%)
  -  Arapahoe: 24,801 (6.7%)

- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
  
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
  - Diana DeGette received 73.8% of the vote with 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
  
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote with 272,892 votes.

## Election-Audit Summary
With a few modifications this script could be used for any election. Row 9 (file_to_load=os.path.join("Resources", "election_results.csv")) could be modified to load data from any election or any year. By using a CSV file containing additional data, such as voter demographics, this script could be modified to determine if a certain candidate received more votes from voters of a certain gender, race, socioeconomic status, etc.
