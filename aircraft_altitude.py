from aircraft import Aircraft

def main():
    model = input("Enter aircraft model: ")
    my_aircraft = Aircraft(model)

    while True:
        user_input = input("Enter command (A for ascent, D for descent, X to exit): ")
        
        parts = user_input.split()
        command = parts[0].upper() 

        if command == 'X':
            break
        
        if len(parts) > 1:
            feet = int(parts[1])
            
            if command == 'A':
                my_aircraft.ascent(feet)
            elif command == 'D':
                my_aircraft.descent(feet)
        else:
            print("Invalid format. Use 'A <feet>' or 'D <feet>'.")

    print(f"Final altitude: {my_aircraft.altitude} feet")

if __name__ == "__main__":
    main()