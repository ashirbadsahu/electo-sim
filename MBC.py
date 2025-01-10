import matplotlib.pyplot as plt

# In modified borda count(MBC), the voters rank the candidates as their preference number
# The candidate with the highest score is the winner
# While there is a limit on how many preferences one can have, which is usually 6.
# One can not assign same preference number to two different candidates.

# Scoring
"""
If there are n candidates and maximum number of preference is m then
1st candidate will get m points
2nd candidate will get m-1 points
.
.
mth candidate will get m-(m-1) points
others will get 0
"""
## Normalization
"""
Let's say one can rank only 6 candidates but he/she decides to rank only 3 of them
Normally only 3 will get points and others will get 0, which is not so fair.
To encounter this normalization is done.

If one has ranked 6 candidates the total points will be: 6+5+4+3+2+1 = 21 points
But in case one ranks only 3 of them it needs to be normalized.

Normalization factor = no of pref one ranked / Max preferences
Here Normalization factor will be 3/6 = 0.5

Without normalization the 3 candidates would have gotten 6, 5, 4 points respectively.
But after normalization they'll get (Normalization factor * Points without normalization)
Now normalized points for, 
Rank 1 candidate: 0.5 * 6 = 3
Rank 2 candidate: 0.5 * 5 = 2.5
Rank 3 candidate: 0.5 * 4 = 2.0
"""
# Let A, B, C, D, E, F, G, H, I, J are 10 candidates.
CANDIDATES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
MAX_PREFERENCES = 6

# initialize candidate scores
candidates = {candidate: 0 for candidate in  CANDIDATES}

def validate_vote(vote):
    """
    Validate that no candidate appears more than once in the same voter's ranking.
    If there are duplicates, return False (invalid vote).
    Otherwise, return True (valid vote).
    """
    # if there are duplicates in the values(rankings), the vote is invalid.
    seen = set()
    for candidate in vote.values():
        if candidate in seen:
            return False # Duplicate candidate found
        seen.add(candidate)
    return True

def poll(votes, candidates):
    for i in range(len(votes)):
        vote = votes[i]
        
        if any(candidate not in CANDIDATES for candidate in vote.values()):
            print(f"Voter {i+1} voted for invalid candidates: {vote.values()}. Skipping...")
            continue

        if not validate_vote(vote):
            print(f"Invalid vote detected from voter {i+1}: {vote}. Skipping...")
            continue

        pref_count = len(votes[i])
        nf = pref_count / MAX_PREFERENCES # Normalization factor

        if pref_count == 0:
            print(f"Voter {i+1} submitted an empty vote. Skipping...")
            continue
            
        for j, candidate in sorted(vote.items()): # Access the dictionary values
            if candidate in candidates:
                candidates[candidate] += nf * (MAX_PREFERENCES - j)


def score_count(candidates):
    """
    Display the final scores
    """
    sorted_candidates = sorted(candidates.items(), key=lambda x: x[1], reverse= True)
    print("\nfinal scores: ")
    for candidate, score in sorted_candidates:
        print(f"{candidate}: {score}")

def plot(candidates):
    x = list(candidates.keys())
    y = list(candidates.values())
    plt.bar(x, y)
    plt.title('Poll statistics')
    plt.xlabel('Candidate Names')
    plt.ylabel('Score')

votes = [
    {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F'},
    {1: 'A', 2: 'D', 3: 'B', 4: 'I', 5: 'E', 6: 'G'},
    {1: 'A', 2: 'H', 3: 'J', 4: 'G', 5: 'B', 6: 'I'},
    {1: 'B', 2: 'C', 3: 'I'},
    {1: 'B', 2: 'C', 3: 'I', 4: 'A', 5: 'B', 6: 'G'},
]

def main():
    poll(votes, candidates)
    score_count(candidates)
    plot(candidates)

if __name__ == "__main__":
    main()
