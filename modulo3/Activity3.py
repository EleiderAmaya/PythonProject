int_value = 15
float_value = 4.1
text_value = "33"

type_of_float_value = type(float_value) # STEP 2: YOUR CODE HERE

# Convert text_value to an integer
text_value_as_int = int(text_value) # STEP 3: YOUR CODE HERE

# Convert int_value to text
int_value_as_text = str(int_value) # STEP 4: YOUR CODE HERE

# DO NOT CHANGE LINES BELOW
# Print the type of float_value
print("float_value type:", type_of_float_value)

# Adding text_value_as_int to int_value
print("Integer addition: Adding text_value_as_int (33) to int_value (15):", text_value_as_int + int_value)

# Adding (concatenating) text values
print("Text addition: Adding text_value (33) to int_value_as_text (15):", text_value + int_value_as_text)