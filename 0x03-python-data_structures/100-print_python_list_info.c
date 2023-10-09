#include <Python.h>

/**
 * print_python_list_info - function
 * @p: value
 */

void print_python_list_info(PyObject *p)
{
	int len, lo;
	int i = 0;
	PyObject *kai;

	len = Py_SIZE(p);
	lo = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %i\n", len);
	printf("[*] Allocated = %i\n", lo);

	while (i < len)
	{
		printf("Element %i: ", i);
		kai = PyList_GetItem(p, i);
		printf(" %s\n", Py_TYPE(kai)->tp_name);
		i++;
	}
}
