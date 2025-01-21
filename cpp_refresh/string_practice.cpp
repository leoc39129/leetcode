#include <iostream>
#include <string>

using namespace std;    // Don't do this for a real C++ project

int main() {
    // Strings are not primitive (built in) data types in C++, it's a class
    // Since strings are classes, you have to import them

    // Declare a string! (standard way)
    string myName = "Leo";
    cout << myName << endl;


    // Varaiables are not pointers! C++ variables store an object, they are not pointers
    // Unlike other languages (Java, Python), where variables are pointers. This allows
    // the use of the constructor when creating a string, as seen below

    // Declare a string using the constructor!
    string myName2("Leo");
    cout << myName2 << endl;

    // As a result of the above, variables cannot be null in C++; myName3 will get the default
    // value of an empty string
    string myName3;
    cout << myName3 << endl;

    // C++, originally called "C with Classes"
    // string = array of characters
    string myName4 = {'L', 'e', 'o'};
    cout << myName4 << endl;

    // Strings are just arrays of characters! Not typically used, since string is a class in C++,
    // it comes with more functionality (see below!)
    char myName5[] = "Leo";     // C string
    cout << myName5 << endl; 

    // You can index into a string in C++ (0-indexed) using [] or the .at() method
    cout << myName[0] << endl;
    cout << myName[1] << endl;
    cout << myName[2] << endl;
    cout << myName[3] << endl;

    cout << myName.at(0) << endl;
    cout << myName.at(1) << endl;
    cout << myName.at(2) << endl;
    //cout << myName.at(3) << endl;

    // Including this line leads to an error! "Leo" has a length of 3 -- notice how using brackets
    // leads to unpredictable behavior, but .at() throws an error when printing index 3

    // Get the number of characters in a string
    cout << myName.length() << endl;
    cout << myName.size() << endl;

    // See if your string is empty
    cout << (myName.length() == 0) << endl;
    cout << (myName == "") << endl;
    cout << myName.empty() << endl;
    cout << myName3.empty() << endl;


    // Strings in C++ are mutable (changeable!) -- when you do this in Python, you make a whole new 
    // string object (which you can also do this in C++, see last lines in this block)
    string hw = "Hello World!";
    hw[1] = '@';
    hw[hw.length() - 1] = '?';
    hw += '!';
    cout << hw << endl;

    string hw_copy = hw + "!!";     // Remember, double quotes and single quotes are NOT the same!
    cout << hw_copy << endl;

    // Important methods:
    hw.insert(2, "Hello");      // defaults to idx 0; order is index, "String you want to insert"
    hw.insert(3, "Hello");

    cout << hw << endl;

    hw.pop_back();
    cout << hw << endl;

    hw.erase(0, 1); // Deleting Characters: (index, how many characters from this index)
    cout << hw << endl;

    // If the string will remain the same and you don't want the ability to change it, declare
    // it as a const, methods to add/erase from that string will throw an error
    const string myPassword = "supersecurepassword";
}