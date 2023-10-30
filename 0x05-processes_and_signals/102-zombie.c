#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite - Runs infinite number.
 * Return: 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes.
 * Return: 0.
 */
int main(void)
{
	pid_t pZombie;
	int i = 0;

	for (; i < 5; i++)
	{
		pZombie = fork();
		if (pZombie > 0)
			printf("Zombie process created, PID: %d\n", pZombie);
		else
			return (0);
	}

	infinite_while();
	return (0);
}
