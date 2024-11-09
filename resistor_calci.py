def display_colors():
    print("\nColor Codes:")
    print("0: Black   1: Brown   2: Red     3: Orange")
    print("4: Yellow  5: Green   6: Blue    7: Violet")
    print("8: Grey    9: White")
    print("For Multiplier, additionally:")
    print("10: Gold   11: Silver")
    
def get_color_value(color_num, band_type="normal"):
    color_values = {
        0: ("Black", 0, 1),
        1: ("Brown", 1, 10),
        2: ("Red", 2, 100),
        3: ("Orange", 3, 1000),
        4: ("Yellow", 4, 10000),
        5: ("Green", 5, 100000),
        6: ("Blue", 6, 1000000),
        7: ("Violet", 7, 10000000),
        8: ("Grey", 8, 100000000),
        9: ("White", 9, 1000000000),
        10: ("Gold", None, 0.1),
        11: ("Silver", None, 0.01)
    }
    
    if color_num in color_values:
        if band_type == "multiplier":
            return color_values[color_num][0], color_values[color_num][2]
        else:
            return color_values[color_num][0], color_values[color_num][1]
    return None, None

def get_tolerance_value(color_num):
    tolerance_values = {
        1: ("Brown", "±1%"),
        2: ("Red", "±2%"),
        3: ("Orange", "±0.05%"),
        4: ("Yellow", "±0.02%"),
        5: ("Green", "±0.5%"),
        6: ("Blue", "±0.25%"),
        7: ("Violet", "±0.1%"),
        8: ("Grey", "±0.01%"),
        10: ("Gold", "±5%"),
        11: ("Silver", "±10%")
    }
    
    if color_num in tolerance_values:
        return tolerance_values[color_num]
    return None, None

def calculate_resistance():
    print("\n=== 4-Band Resistor Calculator ===")
    
    while True:
        try:
            display_colors()
            
            # First Band
            print("\nEnter number for 1st Band Color (0-9):")
            first_band = int(input())
            first_color, first_value = get_color_value(first_band)
            if first_color is None:
                print("Invalid color selection for 1st band!")
                continue
                
            # Second Band
            print("\nEnter number for 2nd Band Color (0-9):")
            second_band = int(input())
            second_color, second_value = get_color_value(second_band)
            if second_color is None:
                print("Invalid color selection for 2nd band!")
                continue
            
            # Multiplier
            print("\nEnter number for Multiplier Color (0-11):")
            mult_band = int(input())
            mult_color, multiplier = get_color_value(mult_band, "multiplier")
            if mult_color is None:
                print("Invalid multiplier selection!")
                continue
            
            # Tolerance
            print("\nEnter number for Tolerance Color (1-8, 10-11):")
            tol_band = int(input())
            tol_color, tolerance = get_tolerance_value(tol_band)
            if tol_color is None:
                print("Invalid tolerance selection!")
                continue
            
            # Calculate resistance
            base_value = int(f"{first_value}{second_value}")
            resistance = base_value * multiplier
            
            # Format the output
            if resistance >= 1000000000:
                formatted_resistance = f"{resistance/1000000000:.2f}G"
            elif resistance >= 1000000:
                formatted_resistance = f"{resistance/1000000:.2f}M"
            elif resistance >= 1000:
                formatted_resistance = f"{resistance/1000:.2f}K"
            else:
                formatted_resistance = f"{resistance:.2f}"
            
            print("\n=== Result ===")
            print(f"1st Band: {first_color}")
            print(f"2nd Band: {second_color}")
            print(f"Multiplier: {mult_color}")
            print(f"Tolerance: {tol_color}")
            print(f"Resistance: {formatted_resistance}Ω {tolerance}")
            
            # Ask if user wants to calculate another
            print("\nCalculate another? (y/n):")
            if input().lower() != 'y':
                break
                
        except ValueError:
            print("Please enter valid numbers!")
            continue

if __name__ == "__main__":
    calculate_resistance()