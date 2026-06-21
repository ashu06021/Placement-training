// Question: Demonstrate Method Overriding

class Vehicle {

    void start() {
        System.out.println("Vehicle Starts");
    }
}

class Car extends Vehicle {

    @Override
    void start() {
        System.out.println("Car Starts");
    }
}

public class PolymorphismDemo {

    public static void main(String[] args) {

        Vehicle v = new Car();

        v.start();
    }
}