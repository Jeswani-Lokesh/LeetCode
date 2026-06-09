class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort products alphabetically
        products.sort()

        # Final answer list
        result = []

        # Current prefix typed so far
        prefix = ""

        # Go through each character in searchWord
        for ch in searchWord:
            # Add current character to prefix
            prefix += ch

            # Store suggestions for this prefix
            suggestions = []

            # Check every product
            for product in products:
                # If product starts with prefix
                if product.startswith(prefix):
                    # Add product to suggestions
                    suggestions.append(product)

                    # Stop after 3 suggestions
                    if len(suggestions) == 3:
                        break

            # Add suggestions for this prefix
            result.append(suggestions)

        # Return all suggestions
        return result