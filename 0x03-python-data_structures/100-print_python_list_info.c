#include <Python.h>

/**
 * print_python_list_info - function
 * @p: value
 */

void print_python_list_info(PyObject *p)
{
	int len = Py_Size(p), lo = ((PyListObject *)p)->allocated;
	int i = 0;
	PyObject *kai = PyList_GetItem(p, i);

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", lo);
	while (i < len)
	{
		print("Element %d: %s\n", i, Py_TYPE(kai)->tp_name);
		i++;
	}
}
