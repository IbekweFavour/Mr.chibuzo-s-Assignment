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

public static boolean isPrime(int primeNumber){
	boolean evenOrFalseNumber = false;
		
	if (primeNumber % 2 == 0){
	return false;
}
	else if (primeNumber % 2 == 1){
	return true;
}
	
	if (primeNumber == 1){
	return false;
	}
	else if (primeNumber == 2){
	return true;
	}

}


public static void main(String... args){
	Scanner usersInput = new Scanner(System.in);

	System.out.print("Enter a number: ");
	int input = usersInput.nextInt();
	System.out.print(isEven(input));

}


}