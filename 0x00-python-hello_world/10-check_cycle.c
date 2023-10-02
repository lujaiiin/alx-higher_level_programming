#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - function
 * @list: value
 * Return: zero
 */

int check_cycle(listint_t *list)
{
	listint_t *luj;

	luj = list;
	while(list && list->next)
	{
		luj = luj->next;
		list = list->next->next;
		if (luj == list)
		{
			return (1);
		}
	}
	return (0);
}
