#include "lists.h"

/**
 * check_cycle - checks whether the list has a cycle in it.
 * @list: linked list to check.
 * Return: 0 if list has no cycle  and 1 if it has cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *pointer1, *pointer2;

	if (list == NULL || list->next == NULL || list->next->next == NULL)
		return (0);
	pointer1 = list->next;
	pointer2 = list->next->next;

	while (pointer2 && pointer1)
	{
		if (pointer2 == pointer1)
			return (1);
		pointer1 = pointer1->next;
		pointer2 = pointer2->next;
		if (pointer2)
		{
			pointer2 = pointer2->next;
		}
	}
	return (0);
}
