
from product_data import products

# TODO: Step 1 - Print out the products to see the data that you are working with.
print("Available products:")
for product in products:
    print(f"- {product['name']}: {product['tags']}")
print()

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []
response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()
  
# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags = set(customer_preferences)
print(f"Your unique preferences: {customer_tags}")

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_product = {
        'name': product['name'],
        'tags': set(product['tags'])  # Convert tags list to set
    }
    converted_products.append(converted_product)

# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))

# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    
    for product in products:
        match_count = count_matches(product['tags'], customer_tags)
        recommendations.append({
            'name': product['name'],
            'matches': match_count
        })
    
    # Sort by match count in descending order (best matches first)
    recommendations.sort(key=lambda x: x['matches'], reverse=True)
    return recommendations

# TODO: Step 7 - Call your function and print the results
print("\nProduct recommendations based on your preferences:")
recommendations = recommend_products(converted_products, customer_tags)

for i, rec in enumerate(recommendations, 1):
    print(f"{i}. {rec['name']} - {rec['matches']} matching preferences")

# DESIGN MEMO:
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#    - Set intersections: Used to efficiently find common tags between customer preferences 
#      and product tags. Sets provide O(1) average lookup time, making intersections much 
#      faster than nested loops through lists.
#    - Loops: Used to iterate through products and build recommendation list. Essential 
#      for processing each product against customer preferences.
#    - Sorting: Used to rank products by match count, putting best matches first for 
#      better user experience.
#    - Set conversion: Eliminated duplicate preferences and enabled fast set operations.
#
# 2. How might this code change if you had 1000+ products?
#    - Consider using dictionaries/hash maps to pre-index products by tags for faster lookups
#    - Implement pagination or limiting results (e.g., top 10 recommendations only)
#    - Add caching for repeated customer preference patterns
#    - Consider using more sophisticated ranking algorithms (weighted tags, popularity scores)
#    - For very large datasets, might need database indexing or search engines like Elasticsearch
#    - Could parallelize the matching process across multiple threads/processes
#    - Memory optimization: process products in batches rather than loading all at once
