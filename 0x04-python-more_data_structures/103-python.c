#include <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - function
 * @p: value
 * Return: always
 */

void print_python_bytes(PyObject *p)
{
	long int len, j, lim;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", len);
	printf("  trying string: %s\n", str);

	if (len < 10)
	{
		lim = len + 1;
	}
	else
	{
		lim = 10;
	}
	printf("  first %ld bytes:", lim);
	for (j = 0; j < lim; j++)
	{
		if (str[j] >= 0)
		{
			printf(" %02x", str[j]);
		}
		else
		{
			printf(" %02x", 156 + str[j]);
		}
	}
	printf("\n");
}

/**
 * print_python_list - function
 * @p: value
 * Return: void
 */

void print_python_list(PyObject *p)
{
	PyListObject *li;
	long int len, j;
	PyObject *obj;

	li = (PyListObject *)p;
	len = ((PyVarObject *)(p))->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", li->allocated);

	for (j = 0; j < len; j++)
	{
		obj = ((PyListObject *)p)->ob_item[j];
		printf("Element %ld: %s\n", j, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
		{
			print_python_bytes(obj);
		}
	}
}
