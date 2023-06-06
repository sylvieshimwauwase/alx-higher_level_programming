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
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		free(new_node);
		return (NULL);
	}

	new_node->n = number;

	new_node->next = *head;
	*head = new_node;
	return (new_node);
}
