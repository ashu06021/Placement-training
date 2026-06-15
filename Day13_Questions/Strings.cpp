#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

void countWordsSpaces(string str)
{
    int spaces = 0;

    for (char ch : str)
    {
        if (ch == ' ')
            spaces++;
    }

    cout << "Number of words: " << spaces + 1 << endl;
    cout << "Number of spaces: " << spaces << endl;
}

void printWordsNewLine(string str)
{
    string word = "";

    for (char ch : str)
    {
        if (ch == ' ')
        {
            cout << word << endl;
            word = "";
        }
        else
        {
            word += ch;
        }
    }

    cout << word << endl;
}

void countAlphabets(string str)
{
    int count = 0;

    for (char ch : str)
    {
        if (isalpha(ch))
            count++;
    }

    cout << "Number of alphabets: " << count << endl;
}

void secondOccurrence(string str)
{
    char ch;
    cout << "Enter alphabet: ";
    cin >> ch;

    int count = 0;

    for (int i = 0; i < str.length(); i++)
    {
        if (tolower(str[i]) == tolower(ch))
        {
            count++;

            if (count == 2)
            {
                cout << "Second occurrence index: " << i << endl;
                return;
            }
        }
    }

    cout << "Second occurrence not found" << endl;
}

void capitalWords(string str)
{
    string word = "";

    for (char ch : str)
    {
        if (ch == ' ')
        {
            for (char c : word)
                cout << (char)toupper(c);

            cout << endl;
            word = "";
        }
        else
        {
            word += ch;
        }
    }

    for (char c : word)
        cout << (char)toupper(c);

    cout << endl;
}

void reverseString(string &str)
{
    reverse(str.begin(), str.end());
    cout << "Reversed String: " << str << endl;
}

void toggleCase(string str)
{
    for (char &ch : str)
    {
        if (islower(ch))
            ch = toupper(ch);
        else if (isupper(ch))
            ch = tolower(ch);
    }

    cout << "Toggle Case String: " << str << endl;
}

void checkAnagram()
{
    string s1, s2;

    cin.ignore();

    cout << "Enter first string: ";
    getline(cin, s1);

    cout << "Enter second string: ";
    getline(cin, s2);

    s1.erase(remove(s1.begin(), s1.end(), ' '), s1.end());
    s2.erase(remove(s2.begin(), s2.end(), ' '), s2.end());

    transform(s1.begin(), s1.end(), s1.begin(), ::tolower);
    transform(s2.begin(), s2.end(), s2.begin(), ::tolower);

    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());

    if (s1 == s2)
        cout << "Strings are Anagrams" << endl;
    else
        cout << "Strings are Not Anagrams" << endl;
}

void vowelIndices(string str)
{
    cout << "Indices of vowels: ";

    for (int i = 0; i < str.length(); i++)
    {
        char ch = tolower(str[i]);

        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            cout << i << " ";
    }

    cout << endl;
}

int main()
{
    string str;

    cout << "Enter a sentence: ";
    getline(cin, str);

    int choice;

    do
    {
        cout << "\n1.Count words and spaces";
        cout << "\n2.Print each word on new line";
        cout << "\n3.Count alphabets";
        cout << "\n4.Index of second occurrence";
        cout << "\n5.Print words in capital case";
        cout << "\n6.Reverse string";
        cout << "\n7.Toggle case";
        cout << "\n8.Check anagram";
        cout << "\n9.Print vowel indices";
        cout << "\n0.Exit";
        cout << "\nEnter choice: ";
        cin >> choice;

        switch (choice)
        {
            case 1:
                countWordsSpaces(str);
                break;

            case 2:
                printWordsNewLine(str);
                break;

            case 3:
                countAlphabets(str);
                break;

            case 4:
                secondOccurrence(str);
                break;

            case 5:
                capitalWords(str);
                break;

            case 6:
                reverseString(str);
                break;

            case 7:
                toggleCase(str);
                break;

            case 8:
                checkAnagram();
                break;

            case 9:
                vowelIndices(str);
                break;

            case 0:
                cout << "Exiting...";
                break;

            default:
                cout << "Invalid Choice";
        }

    } while (choice != 0);

    return 0;
}
