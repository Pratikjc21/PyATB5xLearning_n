browser_name=str(input("Enter Browser name: "))
match browser_name:
    case "Firefox":
        print("Browser is valid\n")
    case "Chrome":
        print("Browser is valid\n")
    case "Edge":
        print("Browser is valid\n")
    case "Opera":
        print("Browser is valid\n")
    case _:
        print("browser is invalid")