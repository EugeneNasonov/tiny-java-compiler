// A test program for TinyJava

class Sum {
  public static void main(String[] a){
	 System.out.println(new Test().sum(10));
  }
}

class Test {
  int sum(int num) {
    int sum;
    sum = 0;
    do {
      sum = sum + num;
      num = num - 1;
	 } while (0 < num);
    return sum;
  }
}
