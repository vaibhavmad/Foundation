# Python Concepts: Module, Class, Object, and More

**Date**: January 24, 2026  
**Purpose**: Understand fundamental Python terms before diving into imports

---

## 🎯 Core Concepts (Building from What You Know)

### **1. Module** 📦

**What it is:**
- A **file** (`.py`) that contains Python code (functions, variables, classes)
- Think of it as a **toolbox** with tools inside

**Example:**
```python
# File: math_module.py (this is a module)
def sqrt(number):
    # ... calculates square root ...
    return result

pi = 3.14159
```

**Real example:**
- `math` is a module (file: `math.py` somewhere in Python)
- It contains functions like `sqrt()`, `floor()`, and variables like `pi`

**When you write:**
```python
import math
```
You're saying: "Load the math module (file) so I can use its tools"

---

### **2. Function** ⚙️ (You already know this!)

**What it is:**
- A **block of code** that does something specific
- You **call** it with `function_name()`

**Example:**
```python
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")  # Call the function
```

**In a module:**
- Modules contain functions
- `math.sqrt()` is a **function** inside the `math` **module**

---

### **3. Class** 🏗️

**What it is:**
- A **blueprint** or **template** for creating objects
- Think: "Recipe for making cookies" (the recipe = class, the cookies = objects)

**Example:**
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says woof!"
```

**Key points:**
- `class Dog:` = "Here's a blueprint for making dogs"
- `__init__` = Special function that runs when you create a dog
- `self.name` = Each dog has its own name
- `bark()` = A function that belongs to the dog (called a "method")

**You haven't learned classes yet** (Day 8), but you'll see them in imports:
```python
from openai import OpenAI  # OpenAI is a CLASS
```

---

### **4. Object (Instance)** 🐕

**What it is:**
- A **specific thing** created from a class
- Think: "A real cookie made from the recipe"

**Example:**
```python
# Using the Dog class above:
my_dog = Dog("Buddy", 3)  # Create an OBJECT (instance)
print(my_dog.name)        # "Buddy"
print(my_dog.bark())     # "Buddy says woof!"
```

**Key points:**
- `my_dog` is an **object** (also called an **instance**)
- It was created from the `Dog` **class**
- Each object has its own data (`name = "Buddy"`, `age = 3`)

**Real example:**
```python
from openai import OpenAI  # Import the CLASS

client = OpenAI(api_key="...")  # Create an OBJECT from the class
response = client.chat.completions.create(...)  # Use the object
```

---

### **5. Package** 📚

**What it is:**
- A **folder** containing multiple modules
- Think: "A library with many books (modules)"

**Example:**
```
openai/          ← This is a PACKAGE (folder)
  ├── __init__.py
  ├── client.py  ← Module 1
  └── api.py     ← Module 2
```

**When you write:**
```python
from openai import OpenAI
```
- `openai` is a **package** (folder)
- `OpenAI` is a **class** inside one of its modules

---

### **6. Method vs Function** 🔧

**Function:**
- Standalone code that does something
- Called: `function_name()`

**Method:**
- A function that **belongs to a class/object**
- Called: `object.method_name()`

**Example:**
```python
# Function (standalone)
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")  # Just call it

# Method (belongs to an object)
class Dog:
    def bark(self):  # This is a METHOD
        return "woof!"

my_dog = Dog()
result = my_dog.bark()  # Call method ON the object
```

**Key difference:**
- Function: `greet("Alice")` ← no object needed
- Method: `my_dog.bark()` ← needs an object first

---

### **7. Attribute vs Variable** 📝

**Variable:**
- A name that holds a value
- Example: `name = "Alice"`

**Attribute:**
- A variable that **belongs to an object**
- Example: `my_dog.name = "Buddy"`

**Example:**
```python
# Variable (standalone)
age = 25

# Attribute (belongs to object)
class Person:
    def __init__(self, name):
        self.name = name  # 'name' is an ATTRIBUTE

person = Person("Alice")
print(person.name)  # Access the ATTRIBUTE
```

---

## 🔗 How They Connect

```
PACKAGE (folder)
  └── MODULE (file)
       ├── FUNCTIONS (standalone code)
       ├── VARIABLES (standalone data)
       └── CLASSES (blueprints)
            └── OBJECTS (instances)
                 ├── METHODS (functions in objects)
                 └── ATTRIBUTES (variables in objects)
```

---

## 📋 Quick Reference Table

| Term | What It Is | Example |
|------|------------|---------|
| **Module** | A file with code | `math.py` |
| **Package** | Folder with modules | `openai/` |
| **Function** | Standalone code block | `sqrt(16)` |
| **Class** | Blueprint for objects | `class Dog:` |
| **Object** | Instance created from class | `my_dog = Dog()` |
| **Method** | Function in a class/object | `my_dog.bark()` |
| **Attribute** | Variable in an object | `my_dog.name` |
| **Variable** | Standalone name → value | `age = 25` |

---

## 🎯 For Imports (What You're Learning Now)

**When you see:**
```python
import math              # Import a MODULE
from math import sqrt    # Import a FUNCTION from module
from openai import OpenAI  # Import a CLASS from package
```

**What's happening:**
- `math` = module (file)
- `sqrt` = function (inside math module)
- `openai` = package (folder)
- `OpenAI` = class (inside openai package)

---

## ✅ Summary

1. **Module** = File with code (toolbox)
2. **Class** = Blueprint for making objects (recipe)
3. **Object** = Specific thing made from class (actual cookie)
4. **Function** = Standalone code (tool)
5. **Method** = Function that belongs to object (tool in the cookie)
6. **Package** = Folder with modules (library)
7. **Attribute** = Variable in object (data in the cookie)
8. **Variable** = Standalone name → value (data)

**For now (Day 4 - Imports):**
- Focus on **modules** and **functions**
- Classes/objects come later (Day 8)
- But now you know what they mean when you see them! 🎉
