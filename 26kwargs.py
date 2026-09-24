def show_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_kwargs(name="Alice", age=25, city="London")
