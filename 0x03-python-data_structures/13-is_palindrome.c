#include "lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	int size;
	int stack[2045];
	int i;

	size = 0;
	if (head == NULL || *head == NULL)
		return (1);

	while (*head != NULL)
	{
		size++;
		stack[size - 1] = (*head)->n;
		head = &(*head)->next;
	}

	for (i = 0; i < size / 2; i++)
	{
		if (stack[i] != stack[size - i - 1])
			return (0);
	}

	return (1);
}
