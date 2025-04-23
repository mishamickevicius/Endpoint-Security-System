/* 

file.cpp 

This file will manage file I/O 
We need a way to save packet data for use such as
a medium between the C++ code and the ML model/agent

This file will have helper functions that should be called by the main program
*/

#include <iostream>
#include <fstream> // Class for managing file operations
#include <string>

/*
Basic function to perform a text file read
*/
std::string readTxtFile(const std::string& fileName) {
    // Blank string used to hold output of txt file
    std::string txtFileResult;
    // Read from text file
    std::ifstream ReadFile(fileName);

    if (!ReadFile) {
        return "Error: Could not open file.\n";
    }

    std::string line; // Temp var
    while (getline (ReadFile, line)) {
        txtFileResult += line + '\n'; 
    }

    ReadFile.close(); // Close the file
    return txtFileResult; // Return results

}

