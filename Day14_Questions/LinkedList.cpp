#include<iostream>
using namespace std;

struct Student
{
    int data;
    Student *next;
};

Student *head = NULL;

// Create Node (Insert at End)
void createNode()
{
    Student *newnode = new Student;

    cout << "Enter data: ";
    cin >> newnode->data;

    newnode->next = NULL;

    if(head == NULL)
    {
        head = newnode;
    }
    else
    {
        Student *temp = head;

        while(temp->next != NULL)
        {
            temp = temp->next;
        }

        temp->next = newnode;
    }

    cout << "Node Created Successfully!\n";
}

// Delete Last Node
void deleteNode()
{
    if(head == NULL)
    {
        cout << "List is Empty!\n";
        return;
    }

    if(head->next == NULL)
    {
        delete head;
        head = NULL;
        cout << "Node Deleted Successfully!\n";
        return;
    }

    Student *temp = head;

    while(temp->next->next != NULL)
    {
        temp = temp->next;
    }

    delete temp->next;
    temp->next = NULL;

    cout << "Node Deleted Successfully!\n";
}

// Display List
void display()
{
    if(head == NULL)
    {
        cout << "List is Empty!\n";
        return;
    }

    Student *temp = head;

    cout << "Linked List: ";

    while(temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }

    cout << endl;
}

int main()
{
    int choice;

    do
    {
        cout << "\n===== MENU =====\n";
        cout << "1. Create Node\n";
        cout << "2. Delete Node\n";
        cout << "3. Display\n";
        cout << "4. Exit\n";
        cout << "Enter Choice: ";
        cin >> choice;

        switch(choice)
        {
            case 1:
                createNode();
                break;

            case 2:
                deleteNode();
                break;

            case 3:
                display();
                break;

            case 4:
                cout << "Exiting...\n";
                break;

            default:
                cout << "Invalid Choice!\n";
        }

    } while(choice != 4);

    return 0;
}
