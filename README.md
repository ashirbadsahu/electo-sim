# Electosim

Electosim is a Python project that simulates different types of voting systems. The project includes implementations of various voting methods, such as the Modified Borda Count (MBC), Quota Borda System (QBS), and Dodgson Method. The goal is to provide a comprehensive understanding of these voting systems through simulation and visualization.

## Voting Systems Implemented

1. **Modified Borda Count (MBC)**:
   - Voters rank candidates based on their preferences.
   - The candidate with the highest score wins.
   - Normalization is applied if a voter ranks fewer candidates than the maximum allowed.

2. **Quota Borda System (QBS)**:
   - A variation of the Borda Count method for multi-winner elections.
   - Incorporates a quota mechanism to ensure proportional representation.
   - Surplus points are redistributed proportionally to other candidates.

3. **Dodgson Method**:
   - Determines a winner by finding the fewest pairwise swaps needed to become a Condorcet winner.
   - Used when there is no clear Condorcet winner.