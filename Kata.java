import java.util.Scanner;

public class Kata{


public static boolean isEven(int number){
	boolean evenOrFalse = false;

	if (number % 2 == 0){
	evenOrFalse = true;
}
	else{
	evenOrFalse = false;
}
	return evenOrFalse;
}

public static boolean isPrime(int primeNUmber){
	boolean evenOrFalseNumber = false;
		
	if (primeNumber == 1){
	evenOrFalseNumber = false;
	}
	else if (primeNumber == 2){
	evenFalseNumber = true;
	}
	return evenOrFalseNumber;	

}


public static void main(String... args){
	Scanner usersInput = new Scanner(System.in);

	System.out.print("Enter a number: ");
	int input = usersInput.nextInt();
	System.out.print(isEven(input));

}


}