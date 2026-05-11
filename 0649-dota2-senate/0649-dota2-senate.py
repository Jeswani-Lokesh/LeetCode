class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Queue for Radiant senators
        radiant = deque()

        # Queue for Dire senators
        dire = deque()

        n = len(senate)

        # Store indices of senators
        for i in range(n):

            if senate[i] == "R":
                radiant.append(i)

            else:
                dire.append(i)

        # Continue until one party is empty
        while radiant and dire:

            # Get front senator from each party
            r_index = radiant.popleft()
            d_index = dire.popleft()

            # Smaller index acts first
            if r_index < d_index:

                # Radiant bans Dire
                # Radiant survives to next round
                radiant.append(r_index + n)

            else:

                # Dire bans Radiant
                # Dire survives to next round
                dire.append(d_index + n)

        # If radiant queue still has senators
        if radiant:
            return "Radiant"

        # Otherwise Dire wins
        return "Dire"