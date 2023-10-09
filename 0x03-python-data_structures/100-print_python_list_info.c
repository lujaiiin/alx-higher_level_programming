#include <Python.h>

/**
 * print_python_list_info - function
 * @p: value
 */

void print_python_list_info(PyObject *p)
{
	int len = Py_Size(p), lo = ((PyListObject *)p)->allocated;
	int i = 0;
	PyObject *kai;

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
