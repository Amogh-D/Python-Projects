if __name__ == '__main__':
    print("Calculator Program")
    print("\nQ to Quit")
    operator = input("Enter Operator (+, -, *, /): ")


    while operator != 'q':
        input_values = [x for x in input("Enter Numbers: ").split()]
        i = 0
        while i < len(input_values):

            total = float(input_values[i])
            input_values.pop(i)
            i += 1
            if operator == "+":
                for num in input_values:
                    total += float(num)
                print(f"Result (A): {total}")
                break

            elif operator == "-":
                for num in input_values:
                    total -= float(num)
                print(f"Result (S): {total}")
                break

            elif operator == "*":
                for num in input_values:
                    total *= float(num)
                print(f"Result (M): {total}")
                break

            elif operator == "/":
                for num in input_values:
                    if float(num) == 0:
                        print("Not divisible.")
                    else:
                        total /= float(num)
                print(f"Result (D): {total}")
                break

        operator = input("Enter Operator [+, -, *, /]: ")


