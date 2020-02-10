#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
/**
 * infinite_while- infinite while
 * Return: always return 0
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
 */
void main(void)
{
	pid_t pid_child;
	int child_status, zombies = 0;

	while (zombies < 5)
	{
		pid_child = fork();
		zombies++;
		if (pid_child == 0)
			exit(0);
		else
		{
			printf("Zombie process created, PID: %d\n", pid_child);
		}
	}
	infinite_while();
}
