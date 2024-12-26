import java.util.Scanner;

public class Logistics{
public static void main(String... args){

System.out.print(logisticService());

}


public static int logisticService(){

Scanner scan = new Scanner(System.in);

System.out.print("Enter a number of Delivery made: ");
int numberOfDelivery = scan.nextInt();



if (numberOfDelivery < 50){
	int amountPerParcel = 160;
	return numberOfDelivery * amountPerParcel + 5000;
}
else if(numberOfDelivery < 59){
	int amountPerParcel = 200;
	return numberOfDelivery * amountPerParcel + 5000;
}
else if (numberOfDelivery < 69){
	int amountPerParcel = 250;
	return numberOfDelivery *amountPerParcel + 5000;
}
else{
	int amountPerParcel = 500;
	return numberOfDelivery * amountPerParcel + 5000;
}



}
}