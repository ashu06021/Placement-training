#include <iostream>
using namespace std;

class Stack
{
    int arr[100];
    int top;

public:
    Stack()
    {
        top = -1;
    }

    void push(int x)
    {
        if (top == 99)
        {
            cout << "Stack Overflow\n";
            return;
        }

        arr[++top] = x;
    }

    void pop()
    {
        if (top == -1)
        {
            cout << "Stack Underflow\n";
            return;
        }

        cout << "Popped Element: " << arr[top--] << endl;
    }

    void peek()
    {
        if (top == -1)
        {
            cout << "Stack is Empty\n";
            return;
        }

        cout << "Top Element: " << arr[top] << endl;
    }

    void display()
    {
        if (top == -1)
        {
            cout << "Stack is Empty\n";
            return;
        }

        cout << "Stack Elements: ";

        for (int i = top; i >= 0; i--)
            cout << arr[i] << " ";

        cout << endl;
    }

    bool isEmpty()
    {
        return top == -1;
    }

    bool isFull()
    {
        return top == 99;
    }

    int size()
    {
        return top + 1;
    }
};

int main()
{
    Stack s;
    int choice, value;

    do
    {
        cout << "\n1. Push";
        cout << "\n2. Pop";
        cout << "\n3. Peek";
        cout << "\n4. Display";
        cout << "\n5. Is Empty";
        cout << "\n6. Is Full";
        cout << "\n7. Size";
        cout << "\n8. Exit";
        cout << "\nEnter Choice: ";
        cin >> choice;

        switch (choice)
        {
            case 1:
                cout << "Enter Value: ";
                cin >> value;
                s.push(value);
                break;

            case 2:
                s.pop();
                break;

            case 3:
                s.peek();
                break;

            case 4:
                s.display();
                break;

            case 5:
                if (s.isEmpty())
                    cout << "Stack is Empty\n";
                else
                    cout << "Stack is Not Empty\n";
                break;

            case 6:
                if (s.isFull())
                    cout << "Stack is Full\n";
                else
                    cout << "Stack is Not Full\n";
                break;

            case 7:
                cout << "Size of Stack: " << s.size() << endl;
                break;

            case 8:
                cout << "Exiting...\n";
                break;

            default:
                cout << "Invalid Choice\n";
        }

    } while (choice != 8);

    return 0;
}
