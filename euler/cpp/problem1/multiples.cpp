/*
 * Problem 1 of Project Euler.
 * https://projecteuler.net/problem=1
*/

#include <iostream>
#include <string>

// Cheap implementation to cast a char 0-9 to an int.
// Doesn't support 10 or higher.
int ctoi(char s) {
    return s - '0';
}

// Take the input from the user as a comma-separared string and parse out
// the integers into an array, such that 3,5 = [3,5]
void parse_multiples(std::string input, int multiples[]) {
    int c = 0;
    int multiples_n = input.length() / 2 + 1;
    for(int i = 0; i < input.length(); i++) {
        if(i % 2 == 0) {
            multiples[c] = ctoi(input[i]);
            c++;
        }
    }
}

// Sum all the numbers 1 .. max which are a multiple of any of the supplied multiples.
// multiples_n exists to avoid array decay when passed into the function.
int sum_multiples(int multiples[], int multiples_n, int max) {
    int total = 0;
    for(int i = 1; i < max; i++) {
        for(int j = 0; j < multiples_n; j++) {
            if(i % multiples[j] == 0) {
                total = total + i;
                break;
            }
        }
    }

    return total;
}

int main() {
    std::string input;
    int max = 0;

    std::cout << "Enter multiples separated by commas, i.e. 3,5: ";
    std::cin >> input;

    std::cout << "Enter max value to sum to (not inclusive), i.e. 1000: ";
    std::cin >> max;

    int multiples_n = input.length() / 2 + 1;
    int multiples[multiples_n];
    parse_multiples(input, multiples);

    int total = sum_multiples(multiples, multiples_n, max);
    std::cout << "The sum of numbers 1 through " << max 
              << " with multiples of " << input 
              << " = " << total << "\n";

    return 0;
}