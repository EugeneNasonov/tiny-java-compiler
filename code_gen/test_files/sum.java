// A test program for TinyJava

class Sum {
  public static void main(String[] a){
	 System.out.println(new Test().gcd(15, 15));
  }
}

class Test {
  int sum(int num) {
    int sum;
    sum = 0;
    while (0 < num) {
      sum = sum + num;
      num = num - 1;
	 }
    return sum;
  }
  int gcd(int a, int b) {
    int rem;
    while (b != 0) {
        rem = a - b * (a / b);
        a = b;
        b = rem;
    }
    return a;
  }
}
