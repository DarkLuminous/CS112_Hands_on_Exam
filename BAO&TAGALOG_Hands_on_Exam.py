print("**************************")
print("|Number System Conversion|")
print("**************************")
print("By: Roger E. Bao Jr. & James Ira A. Tagalog")

print("")
_decimal = int(input("Enter a number:"))
print("")

print("****************************************************************")
print("Decimal Number to Binary Number")
print("Decimal Number to Octal Number")
print("Decimal Number to Hexadecimal Number")
print("****************************************************************")

print("")
_ConverterPicker = int(input(f"How do you want to convert {_decimal}? Enter from [1-3]:"))
print("")

if _ConverterPicker == 1:
    _Ans = bin(_decimal)
    _PConverter = "Binary"

elif _ConverterPicker == 2:
    _Ans = oct(_decimal)
    _PConverter = "Octal"

elif _ConverterPicker == 3:
    _Ans = hex(_decimal)
    _PConverter = "Hexadecimal"

print("****************************************************************")
print("Decimal", _decimal, "Converted to", _PConverter, "Number is", _Ans)
print("****************************************************************")
