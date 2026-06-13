package problemofjava;

class Book {

    String title;
    String author;
    int year;
    boolean available;
    float price;

    
    Book(String title, String author, int year,
         boolean available, float price) {

        this.title = title;
        this.author = author;
        this.year = year;
        this.available = available;
        this.price = price;
    }

    void displayDetails() {
        System.out.println("Title : " + title);
        System.out.println("Author : " + author);
        System.out.println("Year : " + year);
        System.out.println("Price : ₹" + price);
        System.out.println();
    }
}

public class Library {

    public static void main(String[] args) {

        Book book1 = new Book(
                "Java Programming",
                "James Gosling",
                1995,
                true,
                450);

        Book book2 = new Book(
                "Data Structures",
                "Mark Allen Weiss",
                2018,
                true,
                700);

        Book book3 = new Book(
                "Operating Systems",
                "Galvin",
                2015,
                false,
                550);

        Book[] books = {book1, book2, book3};

       
        Book maxBook = books[0];

        for (Book b : books) {
            if (b.price > maxBook.price) {
                maxBook = b;
            }
        }

        System.out.println("Book with Maximum Price:\n");
        maxBook.displayDetails();
    }
}
