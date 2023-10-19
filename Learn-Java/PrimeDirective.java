import java.util.ArrayList;
import java.util.Arrays;
import java.math.BigInteger;

class PrimeDirective {
  
  // Add your methods here:
  public static boolean isPrime(int number) {
    for (int i = 2; i <= number/2; i++) {
      if ((number % i == 0)) { return false; }
    }
    if ((number < 2)) { return false; }
    return true;
  }

  public ArrayList<Integer> onlyPrimes(int[] numbers) {
    ArrayList<Integer> primes = new ArrayList<Integer>();
    for (int number : numbers) {
      if (isPrime(number)) {
        primes.add(number);
      }
    }
    return primes;
  }

  public ArrayList<Integer> firstNPrimesInArray(int[] numbers, int numPrimes) {
    ArrayList<Integer> firstPrimes = new ArrayList<Integer>();
    for (int number : numbers) {
      if (isPrime(number)) { firstPrimes.add(number); }
      if (firstPrimes.size() == numPrimes) { break; }
    }
    return firstPrimes;
  }

  public int[] firstNPrimes(int numPrimes) {
    int[] firstNPrimes = new int[numPrimes];
    firstNPrimes[0] = 2;
    int number = firstNPrimes[0];
    int idx = 1;
    while (firstNPrimes[numPrimes-1] == 0) {
      number++;
      if (isPrime(number)) { 
        firstNPrimes[idx] = number;
        idx++;
      }
    }
    return firstNPrimes;
  }

  public BigInteger[] firstNFibonacciNumbers(int nNums) {
    BigInteger[] firstNNums = new BigInteger[nNums];
    firstNNums[0] = BigInteger.ZERO; firstNNums[1] = BigInteger.ONE;
    if (nNums <= 2) {
      return firstNNums;
    } else {
      for (int i = 2; i < nNums; i++) {
        BigInteger nexNum = firstNNums[i-2].add(firstNNums[i-1]);
        firstNNums[i] = nexNum;
      }
    }
    return firstNNums;
  }

  public ArrayList<Integer> isOddOrEven(int[] numbers, boolean wantEvens) {
    ArrayList<Integer> oddsOrEvens = new ArrayList<Integer>();
    for (int number : numbers) {
      if (wantEvens) {
        if (number % 2 == 0) {
          oddsOrEvens.add(number);
        }
      } else {
        if (number % 2 != 0) {
          oddsOrEvens.add(number);
        }
      }
    }
    return oddsOrEvens;
  }
  
  public static void main(String[] args) {

    PrimeDirective pd = new PrimeDirective();
    System.out.println("7 " + isPrime(7));
    System.out.println("28 " + isPrime(28));
    System.out.println("2 " + isPrime(2));
    System.out.println("0 " + isPrime(0));
    System.out.println("4 " + isPrime(4));
    int[] numbers = {6, 29, 28, 33, 11, 100, 101, 43, 89};
    System.out.println("Primes: "+ pd.onlyPrimes(numbers));
    System.out.println("First 3 Primes: "+ pd.firstNPrimesInArray(numbers, 3));
    System.out.println("Odds: " + pd.isOddOrEven(numbers, false));
    System.out.println("Evens: " + pd.isOddOrEven(numbers, true));
    System.out.println("First Fibs: " + Arrays.toString(pd.firstNFibonacciNumbers(100)));
    System.out.println("First 20 primes: " + Arrays.toString(pd.firstNPrimes(20)));
    
  }  
}