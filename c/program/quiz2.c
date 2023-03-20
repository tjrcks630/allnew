#include<stdio.h>
#include"libcheckprime.h"

void main() {
  int n;
  printf("Input Number : ");
  scanf("%d", &n);
  for(int i=2;i<=n;i++)
  if (n == 0) break;
    if(checkprime(n)==n)
      printf("%d is prime number \n", n);
    else
      printf("%d is no prime number~!! \n", n);
      continue;
}
