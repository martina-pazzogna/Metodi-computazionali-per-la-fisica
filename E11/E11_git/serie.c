//funzione in C che implementa la funzione per calcolare i termini della sequenza di Fibonacci

#include <stdio.h>
#include <math.h>



double fibonacci(int n){
    if (n < 2){
        return 0;
    }
      

    int a = 1;
    int b = 1;
    int term;

    for(int i = 2; i < n; i++){
        term = a + b;
        a = b;
        b = term;
    }

    
    return (double)b/a;
}