/*
 * Problem 2 of Project Euler.
 * https://projecteuler.net/problem=2
*/

#include <iostream>
#include <string>

int main() {
    int max = 0;

    std::cout << "Enter max Fibonacci value to sum to (inclusive): ";
    std::cin >> max;

    int even_sum = 0;

    // We track fibonacci with a and b. We need c to transition the numbers between the two variables.
    int a = 0;
    int b = 1;
    int c = 0;

    std::cout << "Fibonacci: ";

    while (true) {
        c = b;
        b += a;
        a = c;

        if (b > max) {
            break;
        }

        std::cout << b << ", ";

        if (b % 2 == 0) {
            even_sum += b;
        }
    }

    std::cout << "\n" << "The sum of even numbers in Fibonacci up to " << max 
              << " = " << even_sum << "\n";

    return 0;
}