package Day9placement_training;

class SmartPhone {
	public boolean ison;
	public int brightness;

	public void turnOn() {
		ison = true;
		brightness = 100;

	}

	public void status() {
		System.out.println("brightness Status" + (ison ? "ON " : "off ") + "at " + brightness + "%");

	}

}

public class OOPS {
	public static void main(String[] args) {
		
		SmartPhone phone = new SmartPhone();
		
		phone.status();
		phone.turnOn();
		phone.status();

	}
}
