#DECALRE DataArray : ARRAY[0:24] OF INTEGER
DataArray = [] 


def PrintArray(IntArray):
    MyOutput = ""
    for ThisInt in IntArray:
        MyOutput = MyOutput + str(ThisInt) + " "
    print(MyOutput)


def LinearSearch(IntArray, SearchValue):
    Occurrence = 0
    for ThisInt in IntArray:
        if int(ThisInt) == SearchValue:
            Occurrence += 1
    return Occurrence


def main():
    with open("Data.txt") as File:
        for line in File:
            DataArray.append(line.strip())
    PrintArray(DataArray)

    InputError = True
    RangeError = True
    while InputError or RangeError:

        try:
            UserInput = int(input("Whole number between 0 and 100: "))
            InputError = False
        except ValueError:
            print("### Please Re-enter a Integer ###")
        
        if not InputError:
            if UserInput >= 0 and UserInput <= 100:
                RangeError = False 
            else:
                print("### Please Re-enter a Integer between 0 and 100 ###")
        
    print(f"The number {UserInput} is found {LinearSearch(DataArray, UserInput)} times")


main()

