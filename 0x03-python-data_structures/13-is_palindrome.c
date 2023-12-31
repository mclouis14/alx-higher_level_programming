#include "lists.h"
#include <stddef.h>

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *alt = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			alt = slow->next;
			break;
		}
		if (!fast->next)
		{
			alt = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&alt);

	while (alt && temp)
	{
		if (temp->n == alt->n)
		{
			alt = alt->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!alt)
		return (1);

	return (0);
}
