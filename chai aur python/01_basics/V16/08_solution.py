#Function with **kwargs
# Create a function that accepts any number of keyword arguements and prints them in the format key:value.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(power="lazer", name="shaktiman")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy="Dr. Jakaal")
