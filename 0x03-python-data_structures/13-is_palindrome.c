#include "lists.h"
#include <stddef.h>
listint_t *reverse_list(listint_t **head);
int is_palindrome(listint_t **head);
/**
 * reverse_list - a reverse of a singly-linked listint_t list
 * @head: pointer to the starting node of the list in question
 * Return: pointer to the head of the new list after reversal
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *nd = *head, *next, *prv = NULL;

	while (nd)
	{
		next = nd->next;
		nd->next = prv;
		prv = nd;
		nd = next;
	}
	*head = prv;
	return (*head);
}
/**
 * is_palindrome - a function that checks for linked list palidrom
 * @head: pointer to the starting node of the list in question
 * Returns: 1 if found an 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *md, *rv;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}
	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rv = reverse_list(&tmp);
	md = rv;
	tmp = *head;
	while (rv)
	{
		if (tmp->n != rv->n)
			return (0);
		tmp = tmp->next;
		rv = rv->next;
	}
	reverse_list(&md);
	return (1);
}
