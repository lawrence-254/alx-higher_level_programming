#include "lists.h"
/**
 * check_cycle - function in C that checks if a singly linked list has a cycle
 * @list: linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *rev = list;
listint_t *fwd = list;

if (!list)
	return (0);
while(rev&&fwd&&fwd->next)
{
	rev = rev->next;
	fwd = fwd->next->next;
	return (1);
}
return (0);
}
