//Class does...
//addCar function returns true or false based on carType

var ParkingSystem = function (big, medium, small) {
    big = big;
    medium = medium;
    small = small;
};

ParkingSystem.prototype.addCar = function (carType) {
    switch(carType){
        case 1:
            // check if there is space available for this car type
            if (ParkingSystem.big > 0){
                ParkingSystem.big --
                return true     
            } else {
                return false
            }
            break;
        case 2:
            if (ParkingSystem.big > 0){
                ParkingSystem.big --
                return true     
            } else {
                return false
            }
            break;
        case 3:
            if (ParkingSystem.big > 0){
                ParkingSystem.big --
                return true     
            } else {
                return false
            }
            break;
    }
    
}

var obj = new ParkingSystem(1, 1, 0)

