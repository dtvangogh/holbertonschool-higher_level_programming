#include "lists.h"

/**
 * is_palindrome - is the list a palindrome
 * @head: head of the list
 * Return: 1 if True 0 if False
 */

int is_palindrome(listint_t **head)
{
	int size = 0;
	int nums[2048];
	int i;

	if (*head == NULL)
		return (1);

	while (*head != NULL)
	{
		size++;
		nums[size - 1] = (*head)->n;
		head = &(*head)->next;
	}

	int middle = size / 2;

	for (i = 0; i < middle; i++)
	{
		if (nums[i] != nums[size - i - 1])
			return (0);
	}
	return (1);
}
