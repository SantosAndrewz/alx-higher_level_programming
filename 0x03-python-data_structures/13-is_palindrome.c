#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * listint_reverser - reverses the linked list.
 * @head: double pointer to the first node in the linked list.
 *
 * Return: pointer to the first node in the reversed list.
 */
void listint_reverser(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * is_palindrome - checks whether the linked list is a palindrome.
 * @head: double pointer to the linked list.
 *
 * Return: 1 if list is a palindrome, 0 if otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half = NULL;
	listint_t *prev_of_slow = *head;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_of_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		second_half = slow->next;
	}
	else
	{
		second_half = slow;
	}

	prev_of_slow->next = NULL;
	listint_reverser(&second_half);

	while (*head != NULL && second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
		is_palindrome = 0;
		break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}

	listint_reverser(&second_half);

	if (prev_of_slow != NULL)
	{
		prev_of_slow->next = second_half;
	}
	else
	{
		*head = second_half;
	}

	return is_palindrome;
}
