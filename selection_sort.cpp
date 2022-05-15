
#include <iostream>
using namespace std;

void swap(int *a, int *b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

void printArray(int arr[], int n)
{
	for(int i = 0; i<n; i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;
}

void selection_sort(int arr[], int n)
{
	int min_idx;
	for(int i = 0; i<n-1; i++)
	{
		min_idx = i;
		for(int j = i+1; j<n; j++)
		{
			if(arr[min_idx] > arr[j])
			{
				min_idx = j;
			}
		}
		swap(&arr[min_idx], &arr[i]);
	}
}

int main()
{
	int n;
	cout<<"Enter the number of elements in the array: -";
	cin>>n;
	int arr[n];
	for(int i = 0; i<n; i++)
	{
		cout<<"Enter "<<i<<" element of array: -";
		cin>>arr[i];
	}
	cout<<"Array before sorting: -"<<endl;
	printArray(arr, n);
	cout<<"Applying selection sort on array: -";
	selection_sort(arr, n);
	cout<<"\nArray after sorting: -"<<endl;
	printArray(arr, n);
	return 0;
}
