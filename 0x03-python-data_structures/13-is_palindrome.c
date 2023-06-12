#include "lists.h "

/**
 * is_palindrome - checking if it is palindrome
 * @head: head of the linked lists
 *
 * Return: always 1 on sucess
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;

    if (*head == NULL || (*head)->next == NULL)
        return (1);
        
while (fast != NULL && fast->next != NULL)
{
     fast = fast->next->next;
     temp = slow;
     slow = slow->next;
     temp->next = prev;
     prev = temp;
}

if (fast != NULL)
{
    slow = slow->next;
}
 while (slow != NULL)
 {
    if (prev->n != slow->n)
    {
        return 0;
    }
    prev = prev->next;
    slow = slow->next; 
 }
 return 1;
 }
