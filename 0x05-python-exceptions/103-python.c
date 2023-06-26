#include <Python.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *typeName = Py_TYPE(item)->tp_name;
        printf("Element %ld: %s\n", i, typeName);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    char *bytes = PyBytes_AsString(p);

    printf("[.] Bytes object info\n");
    printf("  Size: %ld\n", size);
    printf("  Trying string: %s\n", bytes);

    if (size < 10)
    {
        printf("  First %ld bytes: ", size + 1);
    }
    else
    {
        printf("  First 10 bytes: ");
    }
    for (i = 0; i < size + 1 && i < 10; i++)
    {
        printf("%02hhx ", bytes[i]);
    }
     printf("\n");
}

void print_python_float(PyObject *p)
{
   double value = PyFloat_AsDouble(p);

    printf("[.] Float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }
    printf("  Value: %.16g\n", value);
}