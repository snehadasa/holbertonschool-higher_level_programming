#include "lists.h"

/**
 * insert_node - Inserts a new node
 * @head: head of the linked list
 * @number: number to be inserted
 * Return: new inserted linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *temp2, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	if (head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	if ((*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	temp = *head;
	while (temp && temp->next && temp->next->n < number)
	{
		temp = temp->next;
	}
	temp2 = temp->next;
	temp->next = new_node;
	new_node->next = temp2;
	return (new_node);
}
