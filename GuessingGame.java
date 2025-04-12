import java.util.Scanner;
import java.util.Random;

public class Main {

    public static void CPU1(int tries, int randomNum, Scanner scanner, Random rand, int rangeMin, int rangeMax) {
        int guess;
        while (true) {
            System.out.print("Enter your guess: ");
            if (scanner.hasNextInt()) {
                guess = scanner.nextInt();
            } else {
                System.out.println("Please enter a valid whole number.");
                scanner.next();
                continue;
            }
            tries++;
            if (guess == randomNum) {
                System.out.println("You guessed correctly! The number is " + randomNum);
                System.out.println("Tries: " + tries);
                break;
            } else if (guess < randomNum) {
                System.out.println("Too low, try again.");
            } else {
                System.out.println("Too high, try again.");
            }

            int CPUguess = rand.nextInt(rangeMin, rangeMax + 1);
            if (CPUguess == randomNum) {
                System.out.println("CPU guessed correctly! The number is " + randomNum);
                System.out.println("Tries: " + tries);
                break;
            } else {
                System.out.println("CPU's guess: " + CPUguess);
            }
        }
    }

    public static void CPU2(int tries, int randomNum, Scanner scanner, Random rand, int rangeMin, int rangeMax) {
        int guess;
        while (true) {
            System.out.print("Enter your guess: ");
            if (scanner.hasNextInt()) {
                guess = scanner.nextInt();
            } else {
                System.out.println("Please enter a valid whole number.");
                scanner.next();
                continue;
            }
            tries++;
            if (guess == randomNum) {
                System.out.println("You guessed correctly! The number is " + randomNum);
                System.out.println("Tries: " + tries);
                break;
            } else if (guess < randomNum) {
                System.out.println("Too low, try again.");
            } else {
                System.out.println("Too high, try again.");
            }

            int CPUguess = rand.nextInt(rangeMin, rangeMax + 1);
            if (CPUguess == randomNum) {
                System.out.println("CPU guessed correctly! The number is " + randomNum);
                System.out.println("Tries: " + tries);
                break;
            } else if (CPUguess < randomNum) {
                rangeMin = CPUguess + 1;
            } else {
                rangeMax = CPUguess - 1;
            }
            System.out.println("CPU's guess: " + CPUguess);
        }
    }

    public static void CPU3(int tries, int randomNum, Scanner scanner, Random rand, int rangeMin, int rangeMax) {
        int CPUguess, guess;
        while (true) {
            System.out.print("Enter your guess: ");
            if (scanner.hasNextInt()) {
                guess = scanner.nextInt();
            } else {
                System.out.println("Please enter a valid whole number.");
                scanner.next();
                continue;
            }
            tries++;
            if (guess == randomNum) {
                System.out.println("You guessed correctly! The number is " + randomNum);
                System.out.println("Tries: " + tries);
                break;
            } else if (guess < randomNum) {
                System.out.println("Too low, try again.");
            } else {
                System.out.println("Too high, try again.");
            }

            CPUguess = (rangeMin + rangeMax) / 2;
            if (CPUguess == randomNum) {
                System.out.println("CPU guessed correctly! The number is " + randomNum);
                System.out.println("Tries: " + tries);
                break;
            } else if (CPUguess < randomNum) {
                rangeMin = CPUguess + 1;
            } else {
                rangeMax = CPUguess - 1;
            }
            System.out.println("CPU's guess: " + CPUguess);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random rand = new Random();
        int rangeMin, rangeMax, tries = 0, CPU;

        while (true) {
            System.out.print("Enter the range min: ");
            if (scanner.hasNextInt()) {
                rangeMin = scanner.nextInt();
            } else {
                System.out.println("Please enter a valid whole number.");
                scanner.next();
                continue;
            }

            System.out.print("Enter the range max: ");
            if (scanner.hasNextInt()) {
                rangeMax = scanner.nextInt();
            } else {
                System.out.println("Please enter a valid whole number.");
                scanner.next();
                continue;
            }

            if (rangeMin > rangeMax) {
                System.out.println("Min must be less than max.");
            } else {
                break;
            }
        }

        System.out.print("Choose a CPU (1-3): ");
        CPU = scanner.nextInt();

        int randomNum = rand.nextInt(rangeMax - rangeMin + 1) + rangeMin;

        if (CPU == 1) {
            CPU1(tries, randomNum, scanner, rand, rangeMin, rangeMax);
        } else if (CPU == 2) {
            CPU2(tries, randomNum, scanner, rand, rangeMin, rangeMax);
        } else if (CPU == 3) {
            CPU3(tries, randomNum, scanner, rand, rangeMin, rangeMax);
        } else {
            System.out.println("Invalid CPU selection. Please choose 1, 2, or 3.");
        }

        scanner.close();
    }
}
