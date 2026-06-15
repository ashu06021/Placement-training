#include <stdio.h>
void addition();
void subtraction();
void multiplication();
void division();
void modulus();

int main()
{
    int choice;

    do
    {
        printf("\n===== CALCULATOR MENU =====\n");
        printf("1. Addition\n");
        printf("2. Subtraction\n");
        printf("3. Multiplication\n");
        printf("4. Division\n");
        printf("5. Modulus\n");
        printf("0. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                addition();
                break;

            case 2:
                subtraction();
                break;

            case 3:
                multiplication();
                break;

            case 4:
                division();
                break;

            case 5:
                modulus();
                break;

            case 0:
                printf("Exiting Program...\n");
                break;

            default:
                printf("Invalid Choice! Please try again.\n");
        }

    } while(choice != 0);

    return 0;
}

// Function Definitions

void addition()
{
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d%d", &a, &b);

    printf("Addition = %d\n", a + b);
}

void subtraction()
{
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d%d", &a, &b);

    printf("Subtraction = %d\n", a - b);
}

void multiplication()
{
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d%d", &a, &b);

    printf("Multiplication = %d\n", a * b);
}

void division()
{
    float a, b;

    printf("Enter two numbers: ");
    scanf("%f%f", &a, &b);

    if(b != 0)
        printf("Division = %.2f\n", a / b);
    else
        printf("Division by zero is not allowed!\n");
}

void modulus()
{
    int a, b;

    printf("Enter two numbers: ");
    scanf("%d%d", &a, &b);

    if(b != 0)
        printf("Modulus = %d\n", a % b);
    else
        printf("Modulus by zero is not allowed!\n");
}