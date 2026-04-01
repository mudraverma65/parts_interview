# Task: Dictionary Frequency Mapping
# Instructions: Return a dictionary where keys are categories 
# and values are the count of occurrences.

def count_categories(categories):
    dict_freq = {}
    for s1 in data:
        if s1 in dict_freq:
            dict_freq[s1] += 1
        else:
            dict_freq[s1] = 1

    return dict_freq

# Test Case
data = ['Brakes', 'Engine', 'Brakes', 'Tools', 'Engine', 'Brakes']
# Expected: {'Brakes': 3, 'Engine': 2, 'Tools': 1}
print(count_categories(data))