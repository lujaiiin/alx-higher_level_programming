#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - function
 * @head: value
 * @number: value
 * Return: always
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *okda, *jad;

	jad = malloc(sizeof(listint_t));
	if (!jad)
	{
		return (NULL);
	}
	jad->n = number;
	okda = *head;
	if (okda->n >= number || !okda)
	{
		jad->next = okda;
		*head = jad;
		return (jad);
	}
	while (okda->next->n < number &&
			okda != NULL && okda->next != NULL)
	{
		okda = okda->next;
	}
	jad->next = okda->next;
	okda->next = jad;
	return (jad);
}
