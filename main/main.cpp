#include <iostream>
#include <string>

// Project subfiles 
#include "file.hpp"

int main() {
    std::string result = readTxtFile("tes.txt");
    std::cout << result; 
    return 0;
}