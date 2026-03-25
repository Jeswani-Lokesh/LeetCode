class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the citations in increasing order
        citations.sort()

        # Total number of papers
        n = len(citations)

        # Go through each paper
        for i in range(n):
            # Number of papers from index i to the end
            papers_with_at_least_this_many_citations = n - i

            # If current citation count is enough
            if citations[i] >= papers_with_at_least_this_many_citations:
                # Return the h-index
                return papers_with_at_least_this_many_citations

        # If no valid h-index found, return 0
        return 0
        