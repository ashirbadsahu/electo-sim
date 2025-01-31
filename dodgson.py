# Condorcet winner
# A condorcet winner is a candidate who would win a head-to-head matchup against all other candidates.
"""
Example:
There are 19 people who have to rank 3 candidates according to their preference. They are divided to 3 groups according to their preference order. 
A > B > C means people preferred A over B and B over C.

gr-1: 10 people: A > B > C
gr-2: 5 people: C > A > B
gr-3: 4 people: B > C > A

In a head-to-head matchup,
  1. A vs B: count of A > B from gr-1 and gr-2 is (10+5) = 15 while B > A being 4.
        Here A wins.
  2. B vs C: count of B > C is (10 + 4) = 14 while C > B is 5.
        Here B wins.
  3. A vs C: count of A > C is 10 while C > A is (5+4) = 9.
        Here A wins.

Clearly A won against both B and C in a head-to-head matchup so A is the condorcet winner.
"""

# Dodgson Method
"""
Dodgson method is used when there isn't a clearly one winner. 
The Dodgson's rule determines a winner by finding fewest pairwise swaps in voters preference to become a Condorcet winner.
If a Condorcet winner is decided then it is by default a Dodgson winner.

Example:
There are 15 people who have to rank 3 candidates according to their preference. They are divided to 3 groups according to their preference order. 
A > B > C means people preferred A over B and B over C.

gr-1: 6 people: A > B > C
gr-2: 5 people: C > A > B
gr-3: 4 people: B > C > A

In a head-to-head matchup,
  1. A vs B: count of A > B is 11 while B > A is 4.
      So A wins.
  2. A vs C: count of A > C is 6 while C > A is 9.
      So C wins.
  3. B vs C: count of B > C is 10 while C > B is  4.
      So B wins.

Here we had a paradox, called Condorcet paradox. A is winning against B but loosing against C but B is again winning against C in a head-to-head matchup.
To counter this Dodgson's rule is used.

For A to become Dodgson's winner:
      A already won against B. To win against C, A needs 2 swaps, i.e 2 votes from C will be allocated to A.
      So A requires 2 swaps.

For B to become Dodgson's winner:
      B already won against C. To win against A, 4 swaps are required.
      So B requires 4 swaps.

For C to become Dodgson's winner:
      C has won against A. To win against B, 4 swaps are required.
      So C requirers 4 swaps.

Here A requires least number of swaps, so A is the Dodgson's winner.
"""

# Function to calculate pairwise victory count
def pairwise_wins(rankings, candidate1, candidate2):
    """
    Returns the number of people who prefer candidate1 over candidate2 in a head-to-head matchup.
    """
    count = 0
    for group in rankings:
        count += group.count(candidate1) > group.count(candidate2)
    return count

# Function to calculate the number of swaps needed to make a candidate win a head-to-head matchup
def swaps_needed(rankings, winner, loser):
    """
    Calculate the minimum number of swaps required for 'winner' to win against 'loser'.
    A swap is counted when voters' preferences need to be adjusted to flip the result of the matchup.
    """
    swaps = 0
    for group in rankings:
        if group.index(winner) > group.index(loser):
            swaps += 1
    return swaps

def dodgson_winner(rankings, candidates):
    """
    Determines the Dodgson winner by calculating the minimum number of swaps required for each candidate to become the Condorcet winner.
    """
    swap_counts = {candidate: 0 for candidate in candidates}

    # Check pairwise matchups
    for i, candidate1 in enumerate(candidates):
        for candidate2 in candidates[i+1:]:
            win_count1 = pairwise_wins(rankings, candidate1, candidate2)
            win_count2 = pairwise_wins(rankings, candidate2, candidate1)

            if win_count1 < win_count2:
                swap_counts[candidate1] += swaps_needed(rankings, candidate1, candidate2)
            elif win_count1 > win_count2:
                swap_counts[candidate2] += swaps_needed(rankings, candidate2, candidate1)
    return min(swap_counts, key=swap_counts.get)

# Example usage:
rankings = [
    ['A', 'B', 'C'],  # gr-1: A > B > C (6 people)
    ['C', 'A', 'B'],  # gr-2: C > A > B (5 people)
    ['B', 'C', 'A'],  # gr-3: B > C > A (4 people)
]

candidates = ['A', 'B', 'C']
print(f"The Dodgson winner is: {dodgson_winner(rankings, candidates)}")
