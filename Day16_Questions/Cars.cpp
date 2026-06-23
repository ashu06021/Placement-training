#include <iostream>
#include <string>
using namespace std;

class Car {
private:
    // Identity
    string vin;
    string registrationNumber;

    // Static Attributes
    string brand;
    string model;
    string color;
    string engineType;
    string fuelType;
    int manufacturingYear;

    // Dynamic Attributes
    double speed;
    double fuelLevel;
    double odometerReading;
    double engineTemperature;
    int currentGear;
    string location;
    bool engineOn;

public:
    // Constructor
    Car(string v, string reg, string b, string m,
        string c, string eType, string fType, int year)
    {
        vin = v;
        registrationNumber = reg;
        brand = b;
        model = m;
        color = c;
        engineType = eType;
        fuelType = fType;
        manufacturingYear = year;

        speed = 0;
        fuelLevel = 50;
        odometerReading = 0;
        engineTemperature = 25;
        currentGear = 0;
        location = "Garage";
        engineOn = false;
    }

    // Behaviors (Abstraction)
    void start() {
        if (!engineOn) {
            engineOn = true;
            cout << "Car started.\n";
        }
    }

    void stop() {
        if (engineOn) {
            speed = 0;
            currentGear = 0;
            engineOn = false;
            cout << "Car stopped.\n";
        }
    }

    void accelerate(double increment) {
        if (engineOn) {
            speed += increment;
            fuelLevel -= increment * 0.05;
            cout << "Speed: " << speed << " km/h\n";
        }
    }

    void brake(double decrement) {
        speed -= decrement;
        if (speed < 0)
            speed = 0;

        cout << "Speed: " << speed << " km/h\n";
    }

    void changeGear(int gear) {
        currentGear = gear;
        cout << "Gear changed to " << currentGear << endl;
    }

    void refuel(double amount) {
        fuelLevel += amount;

        if (fuelLevel > 100)
            fuelLevel = 100;

        cout << "Fuel Level: " << fuelLevel << "%\n";
    }

    // Encapsulated access
    double getSpeed() const {
        return speed;
    }

    double getFuelLevel() const {
        return fuelLevel;
    }

    string getVIN() const {
        return vin;
    }

    void displayStatus() {
        cout << "\n----- Car Status -----\n";
        cout << "Brand: " << brand << " " << model << endl;
        cout << "Speed: " << speed << " km/h" << endl;
        cout << "Fuel Level: " << fuelLevel << "%" << endl;
        cout << "Gear: " << currentGear << endl;
        cout << "Location: " << location << endl;
        cout << "Engine: "
             << (engineOn ? "ON" : "OFF") << endl;
    }
};

int main() {
    Car car("VIN12345",
            "MH12AB1234",
            "Toyota",
            "Corolla",
            "White",
            "Petrol",
            "Petrol",
            2022);

    car.start();
    car.changeGear(1);
    car.accelerate(30);
    car.brake(10);
    car.refuel(20);

    car.displayStatus();

    car.stop();

    return 0;
}
