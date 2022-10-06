# Login and Registration System Documentation
### Here I will explain different code components in my program in detail:

#### tkinter: Standard Python interface to the Tcl/Tk GUI toolkit.
#### os: A portable way of using operating system dependent functionality.

### Functions Used In Program:
- ```main()```
- ```register() ```
- ```login()```
- ```register_user()```
- ```login_verify()```
- ```login_success()```
- ```password_not_recognised()```
- ```user_not_found()```
- ```delete_login_success()```
- ```delete_password_not_recognised```
- ```delete_user_not_found_screen```

#### **```global```**: This keyword is used to create global variables from a no-global scope, e.g inside a function.
E.g: 
```python
global username # Exists only once in the script and is visible in every function.
```

#### **```Tk()```**: Displays the root window and manages all other components of the Tkinter application.
E.g:
```python
main_screen = Tk()
```
Syntax:
```python
class Tk(screenName: Optional[str]=..., baseName: Optional[str]=..., className: str=..., useTk: bool=..., sync: bool=..., use: Optional[str]=...)
```

#### **```mainloop()```**: Tells Python to run the Tkinter event loop.
E.g:
```python
main_screen.mainloop() # Keeps looping until program is terminated.
```

Syntax:
```python
def mainloop(self, n: int=...)
```

#### **```pack()```**: Organises widgets in horizontal and vertical boxes that are limited to left, right, top, bottom positions offset and relative to each other within a frame.
```python
Label(text = "Select Your Choice", bg = "aqua", width = "300", height = "2", font =("Helvetica", 15)).pack() # Returns a label allowing you the choice of registering or logging in.
```

#### ```Toplevel()```: Toplevel widget, e.g. for dialogs.
E.g:
```python
register_screen = Toplevel(main_screen)
```

Syntax:
```python
class Toplevel(master: Optional[Any]=..., cnf=..., **kw)
```

#### ```StringVar()```: Value holder for strings variables.
E.g
```python
username = StringVar()
password = StringVar()
```

Syntax:
```python
class StringVar(master: Optional[Any]=..., value: Optional[Any]=..., name: Optional[Any]=...)
```

#### ```listdir()```: Return a list containing the names of the files in the directory.
E.g:
```python
list_of_files = os.listdir() # Returns the files in this Final_Project or any root directory.
```

Syntax:
```python
def listdir(path: Optional[str]=...)
```

```read()```: Reads data previously written to a file.
E.g:
```python
verify = file1.read().splitlines()
```

```splitlines()```: Splits a string into a list.
E.g:
```python
verify = file1.read().splitlines()
```

```if __name__=="__main__"```: Boilerplate code that protects users from accidentally invoking the script when they didn't intend to.