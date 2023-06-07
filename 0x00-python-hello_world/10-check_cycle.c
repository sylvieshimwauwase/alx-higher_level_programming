#include "lists.h"

/**
 * check_cycle - checks if a singly list has a cycle
 * @list: pointer to head
 *
 * Return: 0 when no cycle, 1 when there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
