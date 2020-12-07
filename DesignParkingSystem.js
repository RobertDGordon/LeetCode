//Class does...
//addCar function returns true or false based on carType

var ParkingSystem = function (big, medium, small) {
    this.big = big;
    this.medium = medium;
    this.small = small;
};

ParkingSystem.prototype.addCar = function (carType) {
    switch(carType){
        case 1:
            // check if there is space available for this car type
            if (this.big > 0){
                this.big --
                return true     
            } else {
                return false
            }
            break;
        case 2:
            if (this.medium > 0){
                this.medium --
                return true     
            } else {
                return false
            }
            break;
        case 3:
            if (this.small > 0){
                this.small --
                return true     
            } else {
                return false
            }
            break;
    }
    
}

var obj = new ParkingSystem(1, 1, 0)
console.log(obj.big)

