#include "lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	int size;
	int options[2048];
	int i;

	size = 0;
	if (head == NULL || *head == NULL)
		return (1);

	while (*head != NULL)
	{
		size++;
		options[size - 1] = (*head)->n;
		head = &(*head)->next;
	}

	int middle = size / 2;

	for (i = 0; i < middle; i++)
	{
		if (options[i] != options[size - i - 1])
			return (0);
	}

	return (1);
}
