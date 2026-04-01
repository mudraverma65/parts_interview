# Task: String Formatting
# Goal: Transform a raw SKU into a readable title.

def format_sku(sku_string):
    """
    Instructions: Convert 'engine-oil-10w30' to 'Engine Oil 10w30'.
    """
    words = []
    split_index = 0
    for i in range(0, len(sku_string)):
        word1 = ''
        if sku_string[i] == '-':
            word1 = sku_string[split_index:i]
            split_index = i+1
            words.append(word1.capitalize())
        if i == len(sku_string)-1:
            word1 = sku_string[split_index:i+1]
            words.append(word1.capitalize())    
    
    combined_str = " ".join(word for word in words)
    return combined_str


print(format_sku("brake-pads-ceramic"))