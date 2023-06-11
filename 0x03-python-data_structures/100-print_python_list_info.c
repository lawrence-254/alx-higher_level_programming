#include <Python.h>
/**
 *  print_python_list_info -  a C function that prints
 *  some basic info about Python lists
 *  @p: python object
 */
void print_python_list_info(PyObject *p)
{
	int size, mem, i = 0;
	PyObject *obj;

	size = Py_SIZE(p);
	mem = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", mem);

	while (i < size)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
