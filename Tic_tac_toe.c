/*
     1 | 2 | 3
    ---|---|---
     4 | 5 | 6
    ---|---|---
     7 | 8 | 9
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Display the current board
void print_postion (int * position_list)
{
    printf("\n %s | %s |%s\n---|---|---\n %s | %s | %s\n---|---|---\n %s | %s | %s\n",
                position_list[0], position_list[1], position_list[2],
                position_list[3], position_list[4], position_list[5],
                position_list[6], position_list[7], position_list[8]);
}

// Sort the members in the position list
char * sort (char * position)
{
    char temp;  // For storing the value temporally

    // Bubble sort
    for (int i = 0; i < strlen(position); i++)
    {
        for (int j = i+1; j < strlen(position); j++)
        {
            if (strcmp(position[i], position[j]) > 0)
            {
                temp = position[i];
                position[i] = position[j];
                position[j] = temp;
            }
        }
    }
}

// Check the win status
bool is_win (char * position_list)
{
    sort(position_list);
    int win_position[8][3] = {  {1, 2, 3}, 
                                {4, 5, 6}, 
                                {7, 8, 9}, 
                                {1, 4, 5}, 
                                {2, 5, 8}, 
                                {3, 6, 9},
                                {1, 5, 9},
                                {3, 5, 7}};

    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            for (int k = 0; k < len(position_list); k++)
            {
                
            }
        }
    }
    

}

void one_playyer () 
{
    char position[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    char computer_position[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    bool win = false;
    char playyer_position[5];
    char position;
    printf("Playyer's sign is X and computer sign is O\n");
    do
    {
        for (int i = 0; i < strlen(position); i++)
        {
            printf(" %c | %c | %c\n", position[i+1], position[i + 2], position[i + 3]);
            if (i == 0 || i == 1)
            {
                printf("---|---|---");
            }
        }

        printf("Enter the position number: ");
        scanf("%c", &position);

        

        strcpy(playyer_position, sort(strcat(playyer_position, position)));



    } while (win == false);
    
}

void two_playyer ()
{
    printf()
}
