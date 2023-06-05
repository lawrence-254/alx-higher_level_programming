#ifndef
#define
#include <stdlib.h>
/**
 * struct listint_t - a singly linked list for my python proj
 * @i: an integer
 * @next: pointer to the next node
 */
typedef struct listint_t
{
	int i;
	struct listint_t *next;
} listint_p;

listint_p *add_nodeint(listint_p **head, const int i);
void free_listint(listint_p *head);
size_t print_listint(const listint_p *h);
int check_cycle(listint_p *list);
#endif
