import matplotlib.pyplot as plt
import MBC as mbc

# Quota Borda System (QBS) is a variation of Borda Count voting method that incorporates an additional mechanism to ensure proportional representation in multi-winner elections. QBS should be used when electing more than one person.

"""
Steps:
1. Borda Scoring:
    - The voters rank the candidates as their preference number
    - The candidate with the highest score is the winner
    - While there is a limit on how many preferences one can have, which is usually 6.
    - One can not assign same preference number to two different candidates.
    If there are n candidates and maximum number of preference is m then,
        1st candidate will get m points
        2nd candidate will get m-1 points
        .
        .
        mth candidate will get m-(m-1) points
        others will get 0
2. Calculate Quota:
  - Using Droop quota: Quota = [Total Votes/(Seats + 1)] + 1
  - A candidate must meet or exceed this quota to win a seat.
3. Surplus Calculation:
  - If a candidate's points exceed the quota then the surplus is:
        Surplus = Candidate's Points - Quota
4. Redistribution:
  - The surplus points are distributed proportionally to the other candidates based on their share of votes(or points).
  - For a candidate "X" receiving redistribution:
        Redistribution points to X = Surplus * (Points of X/Total points excluding the winning candidate)
"""

CANDIDATES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
SEATS = 3
MAX_PREFERENCES = 6
VOTES = [
    {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F'},
    {1: 'A', 2: 'D', 3: 'B', 4: 'I', 5: 'E', 6: 'G'},
    {1: 'A', 2: 'H', 3: 'J', 4: 'G', 5: 'B', 6: 'I'},
    {1: 'B', 2: 'C', 3: 'I'},
    {1: 'B', 2: 'C', 3: 'I', 4: 'A', 5: 'K', 6: 'G'},
    {1: 'A', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G'},
    {1: 'B', 2: 'A', 3: 'I', 4: 'J', 5: 'F', 6: 'C'},
    {1: 'B', 2: 'C', 3: 'I', 4: 'A', 5: 'F', 6: 'G'},
    {1: 'B', 2: 'L', 3: 'J', 4: 'A', 5: 'F', 6: 'C'},
]

# Initialize candidate scores
candidates = {candidate: 0 for candidate in CANDIDATES}

def calculate_quota(total_votes, seats):
    return (total_votes / (seats + 1)) + 1

# Distribute surplus points proportionally
def redistribute_surplus(candidates, selected_candidate, surplus_points):
    total_votes = sum(candidates.values())
    if total_votes == 0:  # Avoid division by zero
        return

    for candidate, points in candidates.items():
        if candidate != selected_candidate and points > 0:
            redistribution_ratio = points / total_votes
            candidates[candidate] += surplus_points * redistribution_ratio
    candidates[selected_candidate] = 0

def allocate_seat(candidates, seats):
    allocated = []
    total_votes = sum(candidates.values())
    quota = calculate_quota(total_votes, seats)

    print(f"Quota for seat allocation: {quota}")

    for _ in range(seats):
        selected_candidate, max_score = max(candidates.items(), key=lambda x: x[1])

        if max_score < quota:
            print("Not enough points for further allocation.")
            break

        print(f"Candidate {selected_candidate} wins a seat with {max_score:.2f} points.")
        allocated.append(selected_candidate)

        surplus = max_score - quota
        redistribute_surplus(candidates, selected_candidate, surplus)
    return allocated

def plot_scores(candidates, title):
    x = list(candidates.keys())
    y = list(candidates.values())
    plt.bar(x, y, color='skyblue')
    plt.title(title)
    plt.xlabel("Candidates")
    plt.ylabel("Scores")
    plt.tight_layout()
    plt.show()

def main():
    mbc.poll(VOTES, candidates)
    print("\nScores before seat allocation:")
    mbc.score_count(candidates)

    plot_scores(candidates, "Scores Before Seat Allocation")

    allocated = allocate_seat(candidates, SEATS)
    print(f"\nAllocated seats: {allocated}")

    print("\nScores after seat allocation:")
    mbc.score_count(candidates)
    plot_scores(candidates, "Scores After Seat Allocation")

if __name__ == "__main__":
    main()