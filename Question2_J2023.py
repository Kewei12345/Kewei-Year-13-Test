class Vehicle:

    # DECLARE ID : STRING
    # DECLARE MaxSpeed : INTEGER
    # DECLARE CurrentSpeed : INTEGER
    # DECLARE IncreaseAmount : INTEGER
    # DECLARE HorizontalPosition : INTEGER

    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__IncreaseAmount = IncreaseAmount
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0
    

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    

    def GetMaxSpeed(self):
        return self.__MaxSpeed
    

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    

    def SetCurrentSpeed(self, CurrentSpeed):
        self.__CurrentSpeed = CurrentSpeed


    def SetHorizontalPosition(self, HorizontalPosition):
        self.__HorizontalPosition = HorizontalPosition


    def IncreaseSpeed(self):
        if self.__CurrentSpeed + self.__IncreaseAmount < self.__MaxSpeed:
            self.__CurrentSpeed += self.__IncreaseAmount
        self.__HorizontalPosition += self.__CurrentSpeed


class Helicopter(Vehicle):
    
    # DECLARE VerticalPosition : INTEGER
    # DECLARE VerticalChange : INTEGER
    # DECLARE MaxHeight : INTEGER

    def __init__(self, ID, MaxSpeed, IncreaseAmount, VerticalChange, MaxHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)    

        self.__VerticalChange = VerticalChange
        self.__MaxHeight = MaxHeight
        self.__VerticalPosition = 0


    def GetVerticalPosition(self):
        return self.__VerticalPosition


    def IncreaseSpeed(self):
        if self.__VerticalPosition + self.__VerticalChange < self.__MaxHeight:
            self.__VerticalPosition += self.__VerticalChange
        else:
            self.__VerticalChange = self.__MaxHeight

        if super().GetCurrentSpeed() + super().GetIncreaseAmount() < super().GetMaxSpeed():
            super().SetCurrentSpeed(super().GetCurrentSpeed() + super().GetIncreaseAmount())
        else:
            super().SetCurrentSpeed(super().GetMaxSpeed())

        super().SetHorizontalPosition(super().GetHorizontalPosition() + super().GetCurrentSpeed())
        

def Output(MyVehicle):
    print(f"Your Horizontal Position: {MyVehicle.GetHorizontalPosition()}")
    print(f"Your Speed: {MyVehicle.GetCurrentSpeed()}")
    if str(type(MyVehicle)) == "<class '__main__.Helicopter'>":
        print(f"Your Vertical Position: {MyVehicle.GetVerticalPosition()}")


def main():
    NewCar = Vehicle("Tiger", 100, 20)
    NewHelicopter = Helicopter("Lion", 350, 40, 3, 100)
    NewCar.IncreaseSpeed()
    NewCar.IncreaseSpeed()
    Output(NewCar)
    NewHelicopter.IncreaseSpeed()
    NewHelicopter.IncreaseSpeed()
    Output(NewHelicopter)


main()