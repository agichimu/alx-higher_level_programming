#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }
    
    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
       
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }
    
    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    
    printf("  trying string: ");
    for (Py_ssize_t i = 0; i < 10 && i < size; i++) {
        printf("%02x ", ((unsigned char *)PyBytes_AS_STRING(p))[i]);
    }
    printf("\n");
}


void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[ERROR] Invalid Float Object\n");
        return;
    }
    
    double value = PyFloat_AsDouble(p);
    printf("[.] float object info\n");
    printf("  value: %f\n", value);
}

int main(int argc, char *argv[]) {
    Py_Initialize();

    
    PyRun_SimpleString("l = [1, 2, 3, 4, 5]\n");
    PyObject *list = PyList_New(5);
    for (int i = 0; i < 5; i++) {
        PyList_SetItem(list, i, PyLong_FromLong(i + 1));
    }
    print_python_list(list);
    
    PyRun_SimpleString("b = b'Hello'\n");
    PyObject *bytes = PyBytes_FromString("Hello");
    print_python_bytes(bytes);
    
    PyRun_SimpleString("f = 3.14\n");
    PyObject *flt = PyFloat_FromDouble(3.14);
    print_python_float(flt);

    Py_Finalize();
    return 0;
}
