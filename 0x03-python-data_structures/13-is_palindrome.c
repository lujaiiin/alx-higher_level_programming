#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - function
 * @head: value
 * Return: always
 */

int is_palindrome(listint_t **head)
{
	static int glu[1024];
	listint_t *now;
	int l, i;

	if (head == NULL && *head == NULL)
	{
		return (1);
	}
	now = *head;
	i = 0;
	while (now != NULL)
	{
		now = now->next;
		i++;
	}
	now = *head;
	l = 0;
	i--;
	while (now != NULL)
	{
		if (l <= i)
		{
			glu[l] = now->n;
		}
		else if (glu[i] != now->n)
		{
			return (0);
		}
		now = now->next;
		l++;
		i--;
	}
	return (1);
}
