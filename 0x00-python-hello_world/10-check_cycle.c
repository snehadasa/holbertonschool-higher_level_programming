#include "lists.h"

/**
 * check_cycle - checks whether the list has a cycle in it.
 * @list: linked list to check.
 * Return: 0 if list has no cycle  and 1 if it has cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *temp;

	current = list;
	if (current == NULL)
	{
		return (0);
	}

	while (current->next)
	{
		temp = list;
		if (current == current->next)
			return (1);
		while (temp != current)
		{
			if (temp == current->next)
			{
				return (1);
			}
			temp = temp->next;
		}
		current = current->next;
	}
	return (0);
}
