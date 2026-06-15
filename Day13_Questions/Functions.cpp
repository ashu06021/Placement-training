#include <iostream>
using namespace std;

void displayForward(int arr[], int n) {
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

void displayReverse(int arr[], int n) {
    for(int i = n - 1; i >= 0; i--)
        cout << arr[i] << " ";
    cout << endl;
}

void sortDescending(int arr[], int n) {
    for(int i = 0; i < n - 1; i++) {
        for(int j = i + 1; j < n; j++) {
            if(arr[i] < arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    cout << "Sorted Array: ";
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

void mergeAndMean(int arr[], int n) {
    int n2;
    cout << "Enter size of second array: ";
    cin >> n2;

    int arr2[100], merged[200];

    cout << "Enter second array elements:\n";
    for(int i = 0; i < n2; i++)
        cin >> arr2[i];

    int k = 0, sum = 0;

    for(int i = 0; i < n; i++)
        merged[k++] = arr[i];

    for(int i = 0; i < n2; i++)
        merged[k++] = arr2[i];

    cout << "Merged Array: ";
    for(int i = 0; i < k; i++) {
        cout << merged[i] << " ";
        sum += merged[i];
    }

    cout << "\nMean = " << (float)sum / k << endl;
}

void evenIndex(int arr[], int n) {
    cout << "Even Index Elements: ";
    for(int i = 0; i < n; i += 2)
        cout << arr[i] << " ";
    cout << endl;
}

void sumArray(int arr[], int n) {
    int sum = 0;

    for(int i = 0; i < n; i++)
        sum += arr[i];

    cout << "Sum = " << sum << endl;
}

void search(int arr[], int n) {
    int num;

    cout << "Enter number to search: ";
    cin >> num;

    for(int i = 0; i < n; i++) {
        if(arr[i] == num) {
            cout << "Index Position = " << i << endl;
            return;
        }
    }

    cout << "Number not found!" << endl;
}

void squareArray(int arr[], int n) {
    cout << "Squared Array: ";

    for(int i = 0; i < n; i++)
        cout << arr[i] * arr[i] << " ";

    cout << endl;
}

void deleteElement(int arr[], int &n) {
    int num;
    cout << "Enter number to delete: ";
    cin >> num;

    int pos = -1;

    for(int i = 0; i < n; i++) {
        if(arr[i] == num) {
            pos = i;
            break;
        }
    }

    if(pos == -1) {
        cout << "Number not found!" << endl;
    }
    else {
        for(int i = pos; i < n - 1; i++) {
            arr[i] = arr[i + 1];
        }

        n--;

        cout << "Array after deletion: ";
        for(int i = 0; i < n; i++)
            cout << arr[i] << " ";

        cout << endl;
    }
}

int main() {
    int n, choice;

    cout << "Enter size of array: ";
    cin >> n;

    int arr[100];

    cout << "Enter array elements:\n";
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    do {
        cout << "\n===== MENU =====\n";
        cout << "1. Display Forward\n";
        cout << "2. Display Reverse\n";
        cout << "3. Sort Descending\n";
        cout << "4. Merge Arrays and Find Mean\n";
        cout << "5. Display Even Index Elements\n";
        cout << "6. Sum of Elements\n";
        cout << "7. Search Number and Display Index\n";
        cout << "8. Square of Each Element\n";
        cout << "9. Delete a Number\n";
        cout << "10. Exit\n";
        cout << "Enter Choice: ";
        cin >> choice;

        switch(choice) {
            case 1:
                displayForward(arr, n);
                break;

            case 2:
                displayReverse(arr, n);
                break;

            case 3:
                sortDescending(arr, n);
                break;

            case 4:
                mergeAndMean(arr, n);
                break;

            case 5:
                evenIndex(arr, n);
                break;

            case 6:
                sumArray(arr, n);
                break;

            case 7:
                search(arr, n);
                break;

            case 8:
                squareArray(arr, n);
                break;

            case 9:
                deleteElement(arr, n);
                break;

            case 10:
                cout << "Program Exited Successfully.\n";
                break;

            default:
                cout << "Invalid Choice!\n";
        }

    } while(choice != 10);

    return 0;
}
