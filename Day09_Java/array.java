package typecastin;

public class array {
	class Main {
	    public static void main(String[] args) {
	        String[] food = {"butter chicken","biryani","pizza","pasta","puran poli","bhendi","paneer"};

	food[3] = "Guacamole";

	for(int i = 0; i < food.length; i++) {
	    System.out.println(food[i]);
	}
	    }
	}
}
