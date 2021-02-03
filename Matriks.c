#include <stdio.h>
int main ()
{
	int i, j, k, n;
	float A[20][20], c, x[10];
	
	printf ("\nEnter the size of matrix: ");
	scanf ("%d", &n);
	printf ("\nEnter the elements of augmented matrix row-wise:\n");
	
	for(i=1; i<=n; i++)
	{
		for(j=1; j<=(n+1); j++)
		{
			scanf ("%d", &A[i][j]);
		}
	}
}
