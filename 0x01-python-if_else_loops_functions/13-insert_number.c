#include "lists.h"

/**
 * insert_node - inserts a new node
 * @head: head of node
 * @number: integer number
 *
 * Return: new node created
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *current;

	newNode = malloc(sizeof(listint_t));
	 if (newNode == NULL)
		 return (NULL);

	 newNode->n = number;
	 newNode->next = NULL;

	 if (*head == NULL || number < (*head)->n)
	 {
		 newNode->next = *head;
		 *head = newNode;
		 return (newNode);
	 }

	 current = *head;
	 while (current->next != NULL && current->next->n < number)
		 current = current->next;

	 newNode->next = current->next;
	 current->next = newNode;

	 return (newNode);
}
