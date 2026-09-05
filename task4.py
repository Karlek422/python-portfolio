def calculate_average_speed(distance, time):
    try:
        if time == 0:
            raise ValueError("Time cannot be zero")
        return distance / time
    except ValueError as ve:
        print(f"An error occurred: {ve}")
        return None

result = calculate_average_speed(100, 0)
if result is not None:
    print(result)
else:
    print("An error occurred while calculating average speed.")