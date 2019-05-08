#include "lists.h"

/**
 * copy_list - copies linked list from one to other
 * @start1: start of list1.
 * Return: linked list 2
 */
listint_t *copy_list(listint_t *start1)
{
	listint_t *temp;

	if (start1 == NULL)
		return (NULL);
	temp = malloc(sizeof(listint_t));
	if (!temp)
		return (NULL);

	temp->n = start1->n;
	temp->next = copy_list(start1->next);

	return (temp);
}


/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current, *prev, *next;

	current = *head; /*setting the variable current to head*/

	prev = NULL; /*prev variable to null*/

	while (current != NULL)
	{
		next = current->next; /*storing current in next so we dont loose it*/
		current->next = prev; /*reversing the link and pointing &current to prev*/
		prev = current; /*moving the prev variable to current*/
		current = next; /*moving the current to next variable*/
	}

	*head = prev; /*setting the head to prev*/

	return (*head);
}

/**
 * is_palindrome - Checks whether the list is palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp1, *temp2;

	temp1 = *head;
	temp2 = copy_list(temp1);
	reverse_listint(&temp2);

	while (temp2)
	{
		if (temp1->n != temp2->n)
		{
			return (0);
		}
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	return (1);
}
