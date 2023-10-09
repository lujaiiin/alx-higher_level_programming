#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - function
 * @p: value
 */

void print_python_list_info(PyObject *p)
{
	long int len = PyList_Size(p);
	int i = 0;
	PyListObject *kai = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", kai->allocated);
	while (i < len)
	{
		print("Element %d: %s\n", i, Py_TYPE(kai->ob_item[i])->tp_name);
		i++;
	}
}
