[← Back to Curriculum](../README.md)

---

# Advanced Python & Metaprogramming

- **Decorators & Design Patterns**

  - Function decorators: wraps, functools.lru_cache, property
  - Class decorators: dataclass, total_ordering, modification patterns
  - Parameterized decorators: decorator factories, closure patterns
  - Method decorators: staticmethod, classmethod, cached_property
  - Decorator chaining, order of execution, decorator libraries
  - Common patterns: retry, rate limiting, authentication, caching
  - Performance considerations: decorator overhead, optimization

- **Descriptors & Attribute Access**

  - Descriptor protocol: **get**, **set**, **delete**, **set_name**
  - Data vs non-data descriptors, method resolution order
  - Property implementation using descriptors
  - Validation descriptors, type checking, conversion
  - Attribute access: **getattr**, **setattr**, **delattr**
  - **getattribute** vs **getattr**, attribute lookup chain
  - Slots optimization: **slots**, memory savings, restrictions

- **Metaclasses & Class Creation**

  - Metaclass basics: type as metaclass, **new** vs **init**
  - Custom metaclasses: validation, registration, modification
  - **init_subclass**: simpler alternative to metaclasses
  - Class decorators vs metaclasses: when to use which
  - ABCMeta: abstract methods, registration, subclass checking
  - Singleton patterns, registry patterns using metaclasses
  - Dynamic class creation: type(), exec(), importlib

- **Introspection & Runtime Analysis**

  - `inspect` module: signature, parameters, annotations, source
  - Frame inspection: currentframe, stack, caller information
  - Module introspection: getmembers, isfunction, isclass
  - `dis` module: bytecode disassembly, optimization analysis
  - Code object analysis: co_names, co_varnames, co_code
  - Runtime type checking: isinstance, hasattr, callable
  - Monkey patching: risks, benefits, testing implications

- **Code Generation & AST Manipulation**

  - `ast` module: parse, NodeVisitor, NodeTransformer
  - AST node types: expressions, statements, literals
  - Code generation: compile(), exec(), eval() security
  - Template engines: Jinja2, string.Template, f-strings
  - Dynamic function creation: exec, types.FunctionType
  - Import hooks: importlib, sys.meta_path, finder/loader
  - Source transformation: AST rewriting, code instrumentation

- **C Extensions & Performance**

  - CPython C API: PyObject, reference counting, GIL
  - Cython: .pyx files, static typing, nogil, memoryviews
  - PyO3/Rust: safe bindings, performance, memory management
  - ctypes: foreign function interface, shared libraries
  - CFFI: C Foreign Function Interface, ABI/API modes
  - NumPy C API: ndarray, universal functions, performance
  - Profiling C extensions: gdb, valgrind, performance analysis

- **Memory Management & Optimization**
  - Reference counting: sys.getrefcount, circular references
  - Garbage collection: gc module, generations, thresholds
  - Memory pools: PyMalloc, arena allocator, small object optimization
  - `__slots__`: memory savings, restrictions, inheritance
  - Weak references: weakref module, callbacks, proxy objects
  - Memory leaks: detection, common causes, debugging tools
  - Performance patterns: object pooling, flyweight, interning
