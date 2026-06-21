// Question: Demonstrate Constructor

class Student {

    String name;

    Student(String name) {
        this.name = name;
    }

    void display() {
        System.out.println(name);
    }
}

public class StudentDemo {

    public static void main(String[] args) {

        Student s = new Student("Ashish");
        s.display();
    }
}