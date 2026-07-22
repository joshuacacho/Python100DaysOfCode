# function to return name with title case Ji
def format_name(f_name, l_name):
    title_name_case = f"{f_name} {l_name}"
    return title_name_case.title() # title case

# not saving into variable
print(format_name("JOEY", "LORENZO"))

# saving into variable
output_format_name = format_name("anGOLa", "yU")
print(output_format_name)