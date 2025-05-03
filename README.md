# Virus Scanner Project

Basic Idea: Learn low-level programming using C/C++ and
 use it along with ML to build a Endpoint Security System that
 can detect threats like malware and viruses before they cause damage.
 
 
First Step: Make ML model that can detect Malware/Virus based on certain features
OR: Figure out how to detect using known signatures 

Then build C++ program that takes file/folder of files as input, scan each file,
and if something is detected, create a report using an LLM.


Detailed Approach:

1. Find a public database of Malware/Virus Hashes 
2. Find a way to automatically update the database of hashes
3. Make program to convert files like .exe into hashes
4. Make program to compare hases with database
5. Make program to generate a report with LLMs if a virus match is found. 
