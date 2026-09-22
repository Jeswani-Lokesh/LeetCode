class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank_set = set(bank)                # O(1) validity checks
        if endGene not in bank_set:
            return -1                       # target unreachable
        
        choices = "ACGT"
        queue = deque([(startGene, 0)])     # (gene, mutations so far)
        visited = {startGene}
        
        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            
            # Try mutating each position to each possible base
            for i in range(len(gene)):
                for ch in choices:
                    if ch == gene[i]:
                        continue            # no change → skip
                    mutated = gene[:i] + ch + gene[i+1:]
                    # Valid move: in the bank and not yet visited
                    if mutated in bank_set and mutated not in visited:
                        visited.add(mutated)
                        queue.append((mutated, steps + 1))
        
        return -1                           # exhausted all reachable genes
        