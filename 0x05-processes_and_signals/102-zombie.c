#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - infinite Loop
 * Return: return 0
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
 * main - creation of 5 zombies
 * Return: always 0
 */
int main(void)
{
	pid_t pid_child;
	int child_status, zombies;

	for (zombies = 0; zombies < 5; zombies++)
	{
		pid_child = fork();
		if (pid_child > 0)
			printf("Zombie process created, PID: %d\n", pid_child);
		else
			exit(0);
	}
	infinite_while();

	return (0);
}
