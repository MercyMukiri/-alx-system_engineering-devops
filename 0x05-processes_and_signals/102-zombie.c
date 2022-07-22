#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - creates sleep by running an infinite while loop
 *
 * Return: Always 0
 */

int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - creates 5 zombie processes
 *
 * Return: Always 0
 */

int main(void)
{
	int i;
	pid_t pid;

	i = 0;
	while (i < 5)
	{
		pid = fork();

		if (pid)
		{
			printf("Zombie process created, PID: %i\n", pid);
			i++;
		}
		else
		{
			exit(0);
		}
	}

	infinite_while();

	return (0);
}
